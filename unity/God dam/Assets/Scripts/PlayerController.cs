using System.Collections;
using System.Collections.Generic;
using UnityEngine;

[RequireComponent (typeof (Rigidbody))]
public class PlayerController : MonoBehaviour 
{
	Rigidbody rigidbody;
	Transform character;
	Vector3 velocity;

	void Start ()
	{
		// rigidbody = GetComponent<Rigidbody> ();
		character = GetComponent<Player> ().transform;
	}
	public void Move (Vector3 _velocity)
	{
		velocity = _velocity;
	}

	public void FixedUpdate ()
	{
		// fixedDeltaTime: FixedUpdate 메소드 간의 시간 간격
		// rigidbody.MovePosition (rigidbody.position + velocity * Time.fixedDeltaTime);
		character.Translate(velocity * Time.fixedDeltaTime);
	}
}
