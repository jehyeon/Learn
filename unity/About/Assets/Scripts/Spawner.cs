using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Spawner : MonoBehaviour 
{

	public Transform block;
	public static Spawner instance;

	int rand_shape, rand_pattern;
	bool[] recent = new bool[6];
	
	// void Start () 
	// {
	// 	/////// 블럭 나오는 텀 상수로 고정, 추후 수정
	// 	InvokeRepeating("Spawn", 0, 0.7f);
	// }
	
	void Awake()
	{
		if (Spawner.instance == null)
			Spawner.instance = this;
	}

	// 수정 예정
	// public void RepeatingSpawn()
	// {
	// 	InvokeRepeating("Spawn", 0, 1f);
	// }
	public void Spawn(float blockSpeed)
	{	
		int count = 0;
		foreach (bool element in makePattern())
		{
			if (element == false)
			{
				Vector3 temp = transform.position;
				/////////////// *5 대신 블럭 사이즈로 변경하면 원하는 크기로 게임 수정이 가능 추후 고려
				// 위
				if (count < 3)
				{
					temp += new Vector3((count-1)*5, 5, 0);
				}
				// 아래
				else
				{
					temp += new Vector3((count-4)*5, 0, 0);
				}
				// 블럭 생성
				Transform thisBlock = Instantiate(block, temp, Quaternion.identity);
				thisBlock.GetComponent<Block> ().speed = blockSpeed;

			}
			count++;
		}
		
	}

	// 블럭 패턴 생성
	bool[] makePattern()
	{
		bool[] pattern = new bool[6];
		rand_shape = Random.Range (1, 4);
		rand_pattern = Random.Range (0, rand_shape+1);

		switch (rand_shape)
		{
			// 긴 기둥 1개
			case 1:
				rand_pattern *= 3;	// rand_pattern = 0 or 3
				for (int i = rand_pattern; i < rand_pattern+3; i++)
					pattern[i] = true;
				break;

			// 짧은 기둥 2개
			case 2:
				pattern[rand_pattern] = true;
				pattern[rand_pattern+3] = true;
				break;

			// 긴 기둥 + 짧은 기둥 1개씩
			case 3:
				// 0 1 2 3
				// 0 2 3 5
				if (rand_pattern == 1)
					rand_pattern = 5;
				pattern[rand_pattern] = true;
				break;
		}
		
		bool same = true;
		// recent 패턴과 현재 생성된 패턴 값 비교
		for(int i = 0; i < 6; i++)
		{
			if (recent[i] != pattern[i])
				same = false;
		}

		if (same)
			pattern = makePattern();

		recent = pattern;

		return pattern;
	}
	
}
