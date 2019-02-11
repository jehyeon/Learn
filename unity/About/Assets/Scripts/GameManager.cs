using System.Collections;
using System.Collections.Generic;
using UnityEngine.UI;
using UnityEngine;

public class GameManager : MonoBehaviour {

	private static GameManager _instance = null;
	
	GameObject player;
	GameObject spawner;
	GameObject startingPlane;

	public GameObject resultUIObj;

	float playerH;
	float playerV;
	bool playerIsJumping;
	bool playerIsDie;

	bool gameStarted;		// 게임 시작했는지 여부

	public Text score;
	public Text bestScoreText;
	public Text timeText;

	float actTime;

	float checkTime;

	float upValue;

	float upBlockSpeed = 1.001f;

	float blockSpeed = 30f;


	// Set private variables
	private float bestScore;		// Player's best score, string key name is 'Best Score'

	// Set Single tone
	public static GameManager Instance
	{
		get
		{
			if (_instance == null)
			{
				_instance = FindObjectOfType (typeof (GameManager)) as GameManager;
				if (_instance == null)
				{
					Debug.LogError("There's no active GameManager object");
				}
			}

			return _instance;
		}
	}
	

	void Awake()
	{
		// Set Object
		player = GameObject.FindWithTag("Player");
		spawner = GameObject.FindWithTag("Spawner");
		startingPlane = GameObject.FindWithTag("StartingPlane");

		resultUIObj = GameObject.FindGameObjectWithTag ("ResultUI");
		resultUIObj.SetActive (false);

		// actTime을 -1로 초기화(게임 시작 전)
		actTime = -1;

		checkTime = 0;
		upValue = 1;

		
	}

	void getBestScore()
	{
		if (PlayerPrefs.HasKey("Best Score"))
		{
			bestScore = PlayerPrefs.GetFloat("Best Score");
		}
		else
		{
			bestScore = 0f;
		}
	}

	void setBestScore()
	{
		if (actTime > bestScore)
		{
			bestScore = actTime;
			PlayerPrefs.SetFloat("Best Score", bestScore);
		}
	}

	void Start()
	{
		getBestScore();
	}



	void Update()
	{
		PlayerInput();

		if (actTime > -1 && gameStarted)
		{
			actTime += Time.deltaTime;
		}

		if (gameStarted)
		{
			// // 1초마다
			// spawner.GetComponent<Spawner> ().Spawn();
			
		}

		CheckingDie();
	}

	void FixedUpdate()
	{
		PlayerOutput();

		// Time UI
		if (actTime == -1)
		{
			timeText.text = "";
		}
		else
		{
			timeText.text = actTime.ToString("N2");
		}
		
		if (actTime - checkTime > 0)
		{
			blockSpeed *= upBlockSpeed;
			spawner.GetComponent<Spawner> ().Spawn(blockSpeed);
			player.GetComponent<Player> ().speed *= upBlockSpeed;
			checkTime += upValue;

			if (upValue > 0.5f)
				upValue *= 0.995f;
			// print(blockSpeed);
			// print(player.GetComponent<Player> ().speed);
		}

		if (playerIsDie == true)
		{
			// print("Game Over");
			// print(actTime);
			Time.timeScale = 0;

			// 점수 및 UI 보이기
			setBestScore();
			PlayerPrefs.Save();
			endGame(actTime);
		}
	}

	public bool getStart()
	{
		startingPlane.SetActive(false);
		actTime = 0;
		gameStarted = true;
		return true;
	}
	void PlayerInput()
	{
		// Player Key Input
		playerH = Input.GetAxisRaw("Horizontal");
		playerV = Input.GetAxisRaw("Vertical");

		if (Input.GetButtonDown("Jump"))
		{
			playerIsJumping = true;
		}

		// Player position reset
		// Debug Mode
		// if (Input.GetKeyDown(KeyCode.R))
		// 	player.transform.position = new Vector3(0,1.5f,0);
	}

	// Player Movement
	void PlayerOutput()
	{
		player.GetComponent<Player> ().Move(playerH, playerV);
		if (playerIsJumping == true)
		{
			player.GetComponent<Player> ().Jump();
			playerIsJumping = false;
		}
	}
	void CheckingDie()
	{
		// Player에서 구현하는게 좀 더 이쁠듯
		if (player.GetComponent<Transform> ().position.y < -4)
		{
			player.GetComponent<Player> ().isDie = true;
		}
		playerIsDie = player.GetComponent<Player> ().isDie;
	}

	public void endGame(float _score)
	{
		score.text = _score.ToString("N2");
		bestScoreText.text = bestScore.ToString("N2");
		resultUIObj.SetActive (true);
	}

}
