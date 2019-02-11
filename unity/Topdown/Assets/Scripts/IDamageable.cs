using UnityEngine;

// 인터페이스 파일 앞에는 대문자 'I'가 들어가야 한다.

public interface IDamageable
{
	void TakeHit(float damage, RaycastHit hit);
}