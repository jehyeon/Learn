using System.Collections;
using System.Collections.Generic;
using UnityEngine;

[RequireComponent (typeof (PlayerController))]      // 오브젝트에 스크립트를 더할 때 PlayerController 스크립트까지 강요
[RequireComponent (typeof (GunController))]
public class Player : LivingEntity {

    public float moveSpeed = 5;

    Camera viewCamera;    
    // moveVelocity를 PlayerController로 전달해서 물리적인 부분을 처리하기 위해 
    // PlayerController에 대한 레퍼런스를 가져와야 한다. 
    PlayerController controller;
    GunController gunController;

	protected override void Start () {
        // Player의 부모 클래스(base)의 Start 호출
        base.Start();
        // PlayerController와 Player 스크립트가 같은 오브젝트에 붙어 있는걸 전제로 한다.
        // line:5 를 작성하므로써 아래 코드에 에러가 발생하지 않음
        controller = GetComponent<PlayerController> ();     // GetComponent로 PlayerController 컴포넌트를 가져옴
        gunController = GetComponent<GunController> ();
        viewCamera = Camera.main;
    }

    void Update () {
        // Movement Input
        Vector3 moveInput = new Vector3(Input.GetAxisRaw ("Horizontal"), 0, Input.GetAxisRaw ("Vertical"));
        // 입력의 방향을 얻기 위해 moveInput을 정규화하여 가져온다.
        // normalized는 방향을 가리키는 단위벡터로 만드는 연산
        Vector3 moveVelocity = moveInput.normalized * moveSpeed;
        controller.Move(moveVelocity);

        // Look Input
        Ray ray = viewCamera.ScreenPointToRay (Input.mousePosition);
        Plane groundPlane = new Plane(Vector3.up, Vector3.zero);
        float rayDistance;

        if (groundPlane.Raycast(ray,out rayDistance))
        {
            Vector3 point = ray.GetPoint(rayDistance);
            // Debug.DrawLine(ray.origin, point,Color.red);
            controller.LookAt(point);
        }

        // Weapon Input
        if (Input.GetMouseButton(0))
        {
            gunController.Shoot();
        }
	}
}
