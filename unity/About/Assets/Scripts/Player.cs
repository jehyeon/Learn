using System.Collections;
using System.Collections.Generic;
using UnityEngine.UI;
using UnityEngine;

[RequireComponent (typeof (Rigidbody))]
[RequireComponent (typeof (AudioSource))]
public class Player : MonoBehaviour 
{
	public float speed = 10;
	public float jumpPower = 50;

	Rigidbody rigidbody;
	AudioSource audioSource;

	Vector3 movement;
	
	bool isJumping;
	public bool isDie;
	private float actTime;

	void Awake () 
	{
		actTime = 0;
		rigidbody = GetComponent<Rigidbody> ();
		audioSource = GetComponent<AudioSource> ();
	}
	
	bool CheckGround()
	{
		RaycastHit hit;
		Ray downRay = new Ray(transform.position, -Vector3.up);
		
		if (Physics.Raycast(downRay, out hit))
		{
			if (hit.distance - 0.9f < 1f)
				return true;
		}
		return false;
	}

	// Movement
	public void Move (float horizontal, float vertical)
	{	if (isDie == true)
			return;
		movement.Set (horizontal, 0, vertical);
		movement = movement.normalized * speed * Time.deltaTime;

		rigidbody.MovePosition (transform.position + movement);
	}

	public void Jump ()
	{
		// if (!isJumping)
		// 	return;
		if (CheckGround() == false || isDie == true)
			return;

		rigidbody.AddForce(Vector3.up * jumpPower, ForceMode.Impulse);
		audioSource.Play();
		isJumping = false;
	}

	// Event Trigger
	void OnTriggerEnter(Collider other)
	{
		if (other.gameObject.CompareTag("Area"))
		{
			other.gameObject.SetActive (false);
			GameManager.Instance.getStart();
		}
	}
}
