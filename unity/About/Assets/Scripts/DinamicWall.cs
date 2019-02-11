using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DinamicWall : MonoBehaviour 
{
	private bool isRising;
	private float change_value;
	private float rand;		// Random constant
	private float rising_speed;
	
	void Awake()
	{
		// Set rising speed
		rand = Rangdom.Range(5f, 20f);
		rising_speed = rand;
		isRising = true;	
	}
	
	void Start () 
	{
		StartCoroutine("Dinamic");
	}

	IEnumerator Dinamic()
	{
		while (true)
		{
			// Change the length of a game object at random 
			change_value = rising_speed * Time.deltaTime;
			if (isRising)
			{			
				transform.localScale += new Vector3 (0, change_value, 0);
				transform.position += new Vector3 (0, change_value/2, 0);
			}
			else
			{
				transform.localScale -= new Vector3 (0, change_value, 0);
				transform.position -= new Vector3 (0, change_value/2, 0);
			}

			// Check current status
			if (transform.localScale.y >= 40)
				isRising = false;
			else if (transform.localScale.y <= 20)
				isRising = true;

			yield return new WaitForSeconds(0);
		}
	}

}
