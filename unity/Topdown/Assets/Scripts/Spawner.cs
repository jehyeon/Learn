using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Spawner : MonoBehaviour {

	public Wave[] waves;
	public Enemy enemy;
	
	Wave currentWave;
	int currentWaveNumber;

	int enemiesRemaingToSpawn;
	int enemiesRemainingAlive;
	float nextSpawnTime;

	void Start()
	{
		NextWave();
	}
	void Update()
	{
		if (enemiesRemaingToSpawn > 0 && Time.time > nextSpawnTime )
		{
			enemiesRemaingToSpawn--;
			nextSpawnTime = Time.time + currentWave.timeBetweenSpawns;

			// Quaternion.identity를 지정하여 회전을 주지 않는다.
			Enemy spawnedEnemy = Instantiate(enemy, Vector3.zero, Quaternion.identity) as Enemy;
			spawnedEnemy.OnDeath += OnEnemyDeath;
		}
	}

	void OnEnemyDeath()
	{
		// print ("Enemy died");
		enemiesRemainingAlive --;

		if (enemiesRemainingAlive == 0)
		{
			NextWave();
		}
	}
	void NextWave()
	{
		currentWaveNumber ++;
		print ("Wave: " + currentWaveNumber);
		// currentWaveNumber - 1이 waves의 길이를 초과하지 않도록 만든다.
		if ( currentWaveNumber - 1 < waves.Length)
		{
			currentWave = waves[currentWaveNumber - 1];
			enemiesRemaingToSpawn = currentWave.enemyCount;
			enemiesRemainingAlive = enemiesRemaingToSpawn;
		}
		
	}
	// 추가하므로써 Inspector에서 보이게된다.
	[System.Serializable]
	public class Wave
	{
		public int enemyCount;
		public float timeBetweenSpawns;
	}
}
