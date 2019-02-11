using System.Collections;
using System.Collections.Generic;
using UnityEngine;

// Player는 controller의 component를 가져오므로 해당 컴포넌트가 붙어있도록 설정
[RequireComponent (typeof (PlayerController))]
[RequireComponent (typeof (GunController))]
[RequireComponent (typeof (FPSController))]
public class Player : LivingEntity
{
	PlayerController controller;
	FPSController fpsController;
	GunController gunController;

	public float moveSpeed = 5;

	float mouseX;
	float mouseY;
	float cameraY = 0;

	float sensitivity = 100.0f;

	// LivingEntity의 Start가 덮어지므로 override
	public override void Start () 
	{
		base.Start();
		controller = GetComponent<PlayerController> ();
		gunController = GetComponent<GunController> ();
		fpsController = GetComponent<FPSController> ();
	}
	
	void Update () 
	{
		// 마우스가 화면 밖으로 안 나가게
		Screen.lockCursor = true;

		// Look
		mouseX = Input.GetAxisRaw("Mouse X");
		mouseY = Input.GetAxisRaw("Mouse Y");

		// 100.0f 는 감도 추후 커스텀으로 수정예정
		// 마우스 X는 transform을 회전
		transform.Rotate(Vector3.up * mouseX * sensitivity * Time.deltaTime);
        cameraY -= mouseY  * sensitivity * Time.deltaTime;
        // ?????????? 이해 잘 안감
		if (cameraY < -90)
		{      
            cameraY = -90;
		}
        else if (90 < cameraY)
		{
			cameraY = 90;
		}


		fpsController.MyLook(cameraY);
		// gunController.rotationY(cameraY * -1);

		// Movement Input
		// GetAxisRaw: 기본 스무딩을 적용하지 않음
		Vector3 moveInput = new Vector3 (Input.GetAxisRaw ("Horizontal"), 0, Input.GetAxisRaw ("Vertical"));
		// Vector3 moveVelocity = moveInput.normalized * moveSpeed;	// 입력 값을 단위 벡터로 정규화
		controller.Move (moveInput * moveSpeed);

		// Mouse Input
		if (Input.GetMouseButton (0))
		{
			gunController.Shoot();
		}
	}
}
