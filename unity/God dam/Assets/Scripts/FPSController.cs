using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class FPSController : MonoBehaviour 
{

	public Transform mainCamera;
	public Transform uiCamera;
	
	

	public void MyLook (float cameraY)
	{
		
        mainCamera.localRotation = Quaternion.Euler(cameraY, 0, 0); 
        uiCamera.localRotation = Quaternion.Euler(cameraY, 0, 0);

	}
}
