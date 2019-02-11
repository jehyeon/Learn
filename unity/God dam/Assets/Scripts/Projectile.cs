using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Projectile : MonoBehaviour 
{
	// LayerMask로 어떤 레이어가 발사체와 충돌할지 결정할 수 있다.
	public LayerMask collisionMask;
	float speed = 10;
	float damage = 1;

	public void SetSpeed (float newSpeed)
	{
		speed = newSpeed;
	}
	void Update ()
	{
		// Translate를 호출하기 전에 ray의 이동 거리와 충돌에 대한 결과를 가져와야 한다.
		float moveDistance = speed * Time.deltaTime;
		CheckCollisions (moveDistance);
		transform.Translate(Vector3.forward * moveDistance);		
	}

	void CheckCollisions (float moveDistance)
	{
		Ray ray = new Ray (transform.position, transform.forward);
		// 충돌 오브젝트에 대해 반환한 정보
		RaycastHit hit;

		if (Physics.Raycast(ray, out hit, moveDistance, collisionMask, QueryTriggerInteraction.Collide)) 
		{
			OnHitObject(hit);
		}
	}
	void OnHitObject(RaycastHit hit)
	{
		IDamageable damageableObject = hit.collider.GetComponent<IDamageable> ();
		Debug.Log(damageableObject);
		if (damageableObject != null)
		{
			print(hit);
			damageableObject.TakeHit(damage, hit);
		}
		GameObject.Destroy (gameObject);
	}
	
}
