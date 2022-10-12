# M:N

양쪽 모두에서 N:1의 관계를 가짐

ex) 병원에 내원하는 환자와 의사의 예약 시스템을 구축하기

99_db 폴더 사용



용어

- target model
  - 관계 필드를 가지지 않은 모델
- source model
  - 관계 필드를 가진 모델



실습

- 1번 환자(carol)가 두 의사 모두에게 방문하려 함. 

- N:1 의 한계

  현재 구조로는 같은 환자에 대해 새로운 인스턴스를 만들어서 처리해야 함

  동시에 예약하는 경우 역시 구현 불가능

  => 예약 테이블을 따로 만들자 (예약 : 의사 = N:1,  예약 : 환자 = N:1)

  ```python
  class Reservation(models.Model):
      doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
      patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
  
      def __str__(self):
          return f'{self.doctor_id}번 의사의 {self.patient_id}번 환자'
  ```

  - 의사 입장에서 오늘 예약한 환자 출력 
    - `doctor1.reservation_set.all()`
  - 환자 입장에서도 같음

- 이제 환자 클래스, 의사 클래스에서 직접 예약하는 기능을 구현 (M:N)

  - 환자 모듈에 `  doctors = models.ManyToManyField(Doctor` 추가
  - 그러면 Patient 클래스가 Doctor 클래스 참조, Doctor 클래스는 Patient 역참조
  - 1번 환자가 1번 의사 예약
    - ManyToManyField() 의 add 메서드 활용?
    - `patient1.doctors.add(doctor1)`
  - 의사가 환자 예약
    - `doctor1.patient_set.add(patient2)`
    - ManyToManyFIeld() 가 환자 모듈에 있어서, 의사가 사용하려면 `patient_set`으로 사용해야함 (기능은 똑같이 활용 가능)
  - 예약 삭제
    - `doctor1.patient_set.remove(patient1)`
    - `patient2.doctors.remove(doctor1)`

- 이 때 patinet_set을 patients 로 바꾸는 법

  - related_name 사용
  - ` doctors = models.ManyToManyField(Doctor, related_name='patients') `

django는 ManyToManyField를 통해 중개 테이블을 자동으로 생성



중개모델 직접 작성

- 수동으로 지정하는 경우, through 옵션을 사용하여 django 모델을 지정할 수 있음

- 주로, 중개테이블에 추가 데이터 (예약 시간 등)를 사용해 다대다 관계와 연결하려는 경우

- 실습

  - through 속성 추가

  - ```python
    class Patient(models.Model):
        doctors = models.ManyToManyField(Doctor, related_name='patients', through='Reservetion')        # M:N으로 Doctor 참조
        name = models.TextField()
        def __str__(self):
            return f'{self.pk}번 환자 {self.name}'
    ```

  - 이후 Resrevation 사용

  - ```python
    class Reservation(models.Model):
        doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
        patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
        symptom = models.TextField()
        reserved_at = models.DateTimeField(auto_now_add=True)
    
        def __str__(self):
            return f'{self.doctor_id}번 의사의 {self.patient_id}번 환자'
    ```

정리

- M:N 관계로 맺어진 두 테이블에는 변화 x
- ManyToManyField() 는 중개 테이블을 자동 생성
- M:N 관계를 맺는 두 모델 어디에 위치해도 상관 x, 다만 참조와 역참조 방향 주의
- N:1 은 완전한 종속 관계, M:N 은 상호 종속 관계



ManyToManyField

- 다대다 관계 설정 시 사용하는 모델 필드
- 필수 인자 하나 (M:N 관계로 설정할 모델 클래스)
- 메서드
  - add(), remove(), create(), clear()
  - add()
    - 지정된 객체를 관련 객체 집합에 추가
  - remobe()
    - 관련 객체 집합에서 지정된 모델 개체 제거
    - 내부적으로 QuerySet.delete()를 사용하여 관계가 삭제됨
- 인자
  - related_name
    - target model이 source model 참조할 때 사용할 manager name
  - through
    - 중개 테이블을 직접 작성하는 경우, 이 옵션을 사용하여 중개 테이블을 나타내는 django 모델 지정
  - symmetrical
    - ManyToManyField가 동일한 모델(on self)을 가리키는 정의에서만 사용
    - 트위터의 맞팔을 자동으로 하는 기능?이랄까?
    - 대칭 원하지 않는 경우 False로 구현
- 중개 테이블 필드 생성 규칙
  - source model과 target model이 다른 경우
    - id
    - <containing_model>_id
    - <other_model>_id
  - 동일한 모델인 경우
    - id
    - from\_\<model>_id
    - to\_\<model>_id



### M:N (Article-User)

좋아요 기능과 비슷

04_db 폴더 사용