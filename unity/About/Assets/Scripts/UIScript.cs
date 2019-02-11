using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class UIScript : MonoBehaviour 
{
	// public GameObject imageObj;
	// public Image myImage;
	

	public GameObject musicObj;
	public AudioSource music;
	private bool isPause;

	private static UIScript _instance = null;

	public static UIScript Instance
	{
		get
		{
			if (_instance == null) 
			{
				_instance = FindObjectOfType (typeof(UIScript)) as UIScript;
				if (_instance == null) 
				{
					Debug.LogError ("There's no active UIScript object");
				}
			}	

			return _instance;
		}
	}

	void Awake()
	{
		// imageObj = GameObject.FindGameObjectWithTag("PauseButton");
		// myImage = imageObj.GetComponent<Image> ();
		// score = GameObject.FindGameObjectsWithTag("Score");
		
		musicObj = GameObject.FindGameObjectWithTag("MainMusic");
		music = musicObj.GetComponent<AudioSource> ();

		


	}

	public void PauseButton()
	{
		Image thisImage = this.gameObject.GetComponent<Image> ();
		
		if (isPause == false)
		{
			Time.timeScale = 0;
			// music.Pause();
			thisImage.sprite = Resources.Load<Sprite>("Icons/UI_Icon_Play") as Sprite;
			// Setting UI 팝업 추가 예정
			isPause = true;
		}
		else
		{
			Time.timeScale = 1;
			// music.Play();
			thisImage.sprite = Resources.Load<Sprite>("Icons/UI_Icon_Pause") as Sprite;
			isPause = false;
		}
	}

	public void restartButton()
	{
		Time.timeScale = 1;
		SceneManager.LoadScene (0);
	}
	

	public void reStartButton()
	{
		Debug.Log ("Hello");
	}
}
