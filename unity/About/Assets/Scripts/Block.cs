using System.Collections;
using System.Collections.Generic;
using UnityEngine;

[RequireComponent (typeof (Rigidbody))]
public class Block : MonoBehaviour {

	public float speed = 30;
	
	// Update is called once per frame
	void Update () {
		transform.Translate(Vector3.forward * -1 * speed * Time.deltaTime);	

		if (transform.position.z < -50)
			Destroy(transform.gameObject);
	}
}