using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class GunController : MonoBehaviour {
	public Transform weaponHold;
	public Gun startingGun;
	Gun equippedGun;

	void Start ()
	{
		if (startingGun != null)
		{
			EquipGun(startingGun);
		}
	}
	public void EquipGun(Gun gunToEquip)
	{
		if (equippedGun != null)
		{
			Destroy(equippedGun.gameObject);
		}

		// gunToEquip을 weaponHold의 position과 rotation에 인스턴스 생성
		equippedGun = Instantiate (gunToEquip, weaponHold.position, weaponHold.rotation) as Gun;
		// equippedGun을 Player의 weaponHold의 위치에 따라 움직이도록 weaponHold의 자식으로 설정
		equippedGun.transform.parent = weaponHold; 
	}

	public void Shoot()
	{
		if (equippedGun != null)
		{
			equippedGun.Shoot();
		}
	}

	// public void rotationY (float cameraY)
	// {
	// 	if (equippedGun != null)
	// 	{
	// 		equippedGun.transform.localRotation = Quaternion.Euler(cameraY, 0, 0);
	// 		// Debug.Log(equippedGun.transform.localRotation);
	// 	}
	// }
}
