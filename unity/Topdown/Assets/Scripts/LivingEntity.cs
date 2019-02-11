using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class LivingEntity : MonoBehaviour, IDamageable {
	
	public float startingHealth;
	// 상속 관계 없는 클래스에서 사용할 수 없으며 Inspector에서 볼 수 없음
	protected float health;
	protected bool dead;

	public event System.Action OnDeath;

	// LivingEntity를 상속받는 Player와 Enemy의 Start로 덮어지므로 virtual를 사용한다.
	// 또한 Player와 Enemy의 Start에는 override 키워드를 사용
	protected virtual void Start()
	{
		health = startingHealth;
	}
	public void TakeHit(float damage, RaycastHit hit)
	{
		health -= damage;

		if (health <= 0 && !dead)
		{
			Die();
		}
	}

	protected void Die()
	{
		dead = true;

		if (OnDeath != null)
		{
			OnDeath ();
		}
		GameObject.Destroy(gameObject);
	}
}
