# #던전 입장
# 던전 크기 랜덤 생성, 각 층의 던전 크기 저장
#
# #던전 내 이동
# 던전 내 이동시 20%이동, 20% 포션 획득, 10% 텐트획득, 30% 일반몬스터 만남, 20% 타수호대 만남
# 전투를 안하는 동안 포션사용 및 착장 교체 가능
# 일반몬스터 혹은 타수호대 만나면 전투 시작
#
# #타수호대와 조우 시 전투 세팅
#
# #일반몬스터 조우 시 전투 세팅

# #보스 모스터 위치 지정
# 보스 위치 도달하면 보스전 시작
# 보스전 이기면 다음층 올라가는 입구 열림
# #윗층 이동
# 위로 올라가는 계단 입구 랜덤 생성 및 위치 표시
# 전투 7번까지는 다음층 계단 유지, 8번째 전투부터 다음층 계단 위치 변경
# 보스 죽이기 전에는 접근해도 들어갈 수 없음

#
# #전투불능 상태
# 던전에서 전투 중 전투불능 상태(전원 hp가 0)인 경우 전투가 강제종료되어 던전으로 돌아옴(주양)
# 던전에서 부활포션 유무 판단, 있으면 사용하고 없으면 필드로 보냄
# (진영 필드에서 랜덤배치 및 전투배제모드, 텐트 유무 판단 후 텐트조차 없으면 게임오버)
#
# #최종장
# 7층에서 최종보스 죽인후 8층 이동
# 8층 4*4 크기의 던전에서 복이 위치 표시
# 복이 좌표에 다가가 구출, 게임엔딩
