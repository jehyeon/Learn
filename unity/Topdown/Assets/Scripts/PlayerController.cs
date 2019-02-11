using System.Collections;
using System.Collections.Generic;
using UnityEngine;

[RequireComponent (typeof (Rigidbody))]
public class PlayerController : MonoBehaviour {

	Vector3 velocity;
	// Rigidbody를 사용해서 충돌에 영향을 받도록 하고자 함
	Rigidbody myRigidbody;
	
	void Start () 
	{
		myRigidbody = GetComponent<Rigidbody> ();	
	}
	
	public void Move(Vector3 _velocity)
	{
		velocity = _velocity;
	}

	public void LookAt(Vector3 lookPoint)
	{
		Vector3 heightCorrectedPoint = new Vector3 (lookPoint.x, transform.position.y, lookPoint.z);
		transform.LookAt (heightCorrectedPoint);
	}
	// FixedUpdate를 사용해야 하는 이유는, 이 부분은 정기적이고 짧게 반복적으로 실행되어야 하기 때문
	// FixedUpdate를 써서 프레임 저하가 발생해도 프레임에 시간의 가중치를 곱하여 실행한다면 이동 속도가 유지됨
	private void FixedUpdate()
	{
		// myRigidbody 위치 + 속도 (velocity * 시간 간격) 
		myRigidbody.MovePosition(myRigidbody.position + velocity * Time.fixedDeltaTime);
		// fixedDelteTime은 두 FixedUpdate 메소드가 호출된 시간 간격을 의미함
	}
}
