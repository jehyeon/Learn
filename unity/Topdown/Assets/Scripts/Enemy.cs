using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.AI;

[RequireComponent (typeof (NavMeshAgent))] 
public class Enemy : LivingEntity {

	public enum State {Idle, Chasing, Attacking};
	State currentState;

	NavMeshAgent pathfinder;
	Transform target;
	
	// 1.5 meter
	float attackDistanceThreshold = .5f;
	float timeBetweenAttacks = 1;
	float nextAttackTime;
	float myCollisionRadius;
	float targetCollisionRadius;

	protected override void Start () {
		base.Start();
		pathfinder = GetComponent<NavMeshAgent> ();

		currentState = State.Chasing;
		target = GameObject.FindGameObjectWithTag("Player").transform;

		myCollisionRadius = GetComponent<CapsuleCollider> ().radius;
		targetCollisionRadius = GetComponent<CapsuleCollider> ().radius;

		StartCoroutine (UpdatePath ());
	}
	
	// Update 안에 SetDestination을 호출하는 것은 매 프레임마다 새롭게 경로를 계산하는 것을 의미
	// 이는 매우 비싼 처리를 요구 한다
	void Update () {
		// 제곱근 형태로 거리 계산 시 처리 비용이 비싸다.
		// 벡터 간의 거리 = ((x-x')^2 + (y-y')^2 + ...)^(-2)
		// Vector3.Distance()
		if (Time.time > nextAttackTime )
		{
			float sqrDstToTarget = (target.position - transform.position).sqrMagnitude;

			if (sqrDstToTarget < Mathf.Pow (attackDistanceThreshold + myCollisionRadius + targetCollisionRadius, 2))
			{
				nextAttackTime = Time.time + timeBetweenAttacks;
				StartCoroutine(Attack());
			}
		}
	}
		
	IEnumerator Attack()
	{
		currentState = State.Attacking;
		// 공격 중에는 위치 계산을 원하지 않으므로 false 시킴
		pathfinder.enabled = false;

		Vector3 originalPostion = transform.position;
		Vector3 dirToTarget = (target.position - transform.position).normalized;
		Vector3 attackPosition = target.position - dirToTarget * (myCollisionRadius + targetCollisionRadius);

		float attackSpeed = 3;
		float percent = 0;
		
		// Coroutine이기 때문에 yield return null을 사용한다.
		// 이는 while 루프의 각 처리 사이의 프레임을 스킵한다.
		while (percent <= 1)
		{
			percent += Time.deltaTime * attackSpeed;
			// origin -> attack position 이 후 다시 attack -> origin position으로 이동한다.
			// 대칭 함수를 이용
			float interpolation = (-Mathf.Pow(percent,2) + percent) * 4;

			// Lerp 메소드는 두 벡터 사이에 비례 값으로 내분점 지점을 반환
			transform.position = Vector3.Lerp(originalPostion, attackPosition, interpolation);
			yield return null;
		}

		currentState = State.Chasing;
		pathfinder.enabled = true;
	}

	// 따라서 1초마다 경로를 재계산한다.
	IEnumerator UpdatePath()
	{
		float refreshRate = .25f;

		while (target != null)
		{
			if (currentState == State.Chasing )
			{
				Vector3 dirToTarget = (target.position - transform.position).normalized;
				Vector3 targetPosition = target.position - dirToTarget * (myCollisionRadius + targetCollisionRadius + attackDistanceThreshold/2);
				if (!dead)
				{
					pathfinder.SetDestination (targetPosition);
				}
			}
			yield return new WaitForSeconds(refreshRate);
		}
	}
}
