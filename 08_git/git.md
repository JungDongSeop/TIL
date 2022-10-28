## Git undoing

git 되돌리기는 작업 상태에 따라 크게 3가지로 분류

- working Directory 작업 단계 (작업 폴더)
  - `git restore`
- Staging Area 작업 단계 (add 했을 때 저장되는 곳)
  - Staging Area에 반영된 파일을 Working Directory 로 되돌리기
  - `git rm --cached`
  - `git restore -- staged`
- Repository 작업 단계
  - 커밋 완료한 파일을 Staging Area로 되돌리기
  - `git commit --amend`



#### Git restore

실습

- 빈 폴더 만들고 git init, `touch a.md` 해서 빈 마크다운 파일 만들기
- `git add .` 해서 working directory의 파일을 Stagin Area에 올리기()
- vim 으로 md 파일 수정
  - `vim a.md` 하고 insert 키 눌러서 수정하도록 바꾸고 수정 내용 입력, 이후 esc 키, `:wq`입력

- (중요) 이 때, a.md 수정하고 `git restore a.md` 입력 시, 수정한 파일이 아닌, 커밋 한 상태의 파일 상태로 되돌려짐
  - 하지만, 이전에 작업한 내용은 사라짐. 백업 or 신중히 사용



#### Staging Area 에서 되돌리기

Staging Area에 반영된 파일을 Working Directory로 되돌리기 

- git add 한 내용을 지우고 싶을 때

root-commit (이전 커밋을 했나 안했나) 에 따라 명령어가 나뉨

- root commit 없음 : `git rm --cached`
  - 비교 대상이 없으니, 그냥 caching 되어있는 정보를 삭제(remove)해버리는 것
- root commit 있음 : git restore --staged
  - 

실습

- 새 폴더에서 다시 `git init`, a.md 만들기
- `git rm --cached a.md` 하면 a.md 는 unstage 상태가 됨 (전후 `git status` 해서 비교)
- (rm 은 git 원격저장소에서 지우는 명령어. root commit 안했을 때만 조심해서 사용)



#### Repository 작업 단계에서 되돌리기

 커밋 완료한 파일을 Staging Area로 되돌리기

상황 별로 두 가지 기능으로 나뉨

- Staging Area에 새로 올라온 내용이 없다면, 직전 커밋의 메시지만 수정
- Staging Area에 새로 올라온 내용이 있다면, 직전 커밋을 덮어쓰기 

이전 커밋을 완전히 고쳐서 새 커밋으로 변경하니, 이전 커밋은 사라짐



실습

그냥 커밋 명만 바꾸기

- commit 명을 "second commit" 으로 설정
- `git commit --amend` 한 뒤 insert 키 누르고 commit 명 'third commit'으로 수정, esc키, `:wq` 입력
- 그 뒤 `git log --oneline` 해보면 커밋 명 바뀜

내용도 바꾸고 커밋 수정

- 커밋 'forth commit' 하고 a.md 수정
- b.md 파일 새로 수정
- 그런데 생각해보니 이번 커밋에 b.md도 같이 한번에 커밋해야 했다?
- `git add .` 해서 b.md를 Staging Area에 올리고, `git commit --amend` 한 뒤 저절로 켜진 vim 끄기 (커밋명은 그대로 할 거니까)
- 이러면 commit 안에 b.md도 같이 포함됨



## Git reset & revert



#### Git reset

시계를 돌리듯이, 프로젝트를 특정 커밋(버전) 상태로 되돌림

특정 커밋으로 되돌아 갔을 때, 해당 커밋 이후로 쌓았던 커밋들은 전부 사라짐

`git reset [옵션] {커밋 ID}`

- 옵션은 soft, mixed, hard
- 커밋 ID는 되돌아가고 싶은 시점의 커밋 ID



- --soft
  - 해당 커밋으로 되돌아가고
  - 되돌아간 커밋 이후 파일들은 Staging Area로 돌려놓음 
  - b.md는 이번 커밋에 가면 안되는데 커밋한 경우, soft로 되돌리고 다시 요령껏 커밋
- --mixed
  - 해당 커밋으로 되돌아가고
  - 되돌아간 커밋 이후의 파일들은 Working Directory로 돌려놓음
  - git reset 옵션의 기본값
  - 바뀐 파일은 Staging Area에 저장됨
- --hard
  - 해당 커밋으로 되돌아가고
  - 되돌아간 커밋 이후의 파일들은 모두 Working Directory에서 삭제 
  - 만들었던 파일이 전부 사라지니 주의해서 사용



여태 한 커밋은 전부 .git에 저장됨

git reflog 로 과거 커밋 내역 조회 가능



#### Git revert

과거를 없었던 일로 만드는 행위로, 이전 커밋을 취소한다는 새로운 커밋을 생성

`git revert {커밋 ID}`

reset과의 차이

- reset은 커밋 내역을 삭제, revert는 새로운 커밋을 생성
- revert는 Github을 이용해 협업할 때, 커밋 내역의 차이로 인한 충돌을 방지



실습

- revert zip 파일 압축 해제
- `git revert 6baf32f`
- `git log --oneline` 하면 새로운 커밋 `Revert "second"` 생김
- 그런데 Working Directory에 만들어둔 2.txt 가 사라짐
- `git revert --no-commit {Revert "second" 의 커밋 ID}` 입력하면, revert한 커밋도 지울 수 있음
- 즉, Working Directory에서 사라진 파일이 다시 생성됨



그냥 쓰면 안됨.(Working Directory 안의 파일도 삭제되는 경우 있음)

## Git branch & merge



#### branch

여러 갈래로 작업 공간을 나누어 독립적으로 작업할 수 있도록 도와주는 Git의 도구

여태까지 쓴 git은 혼자 작업하는 거니 branch가 필요없음

장점

- 독립 공간을 형성하기 때문에 원본에 대해 안전함
- 하나의 작업은 하나의 브랜치로 나누어 진행되므로 체계적인 개발이 가능함



실습

- init, add, commit 하기. 이후엔 만들어진 commit이 분화됨
- 브랜치 만들기 : `git branch {브랜치 명}`
- 브랜치 목록 보기 : `git branch`
- 브랜치 삭제 : `git branch -d {브랜치 명}`
- 브랜치 작업공간으로 이동 : `git switch {브랜치 명}`
  - 작업 공간 이동 시, Working Directory의 파일들도 해당 가지에 맞게 나타남
  - 해당 작업 공간에서 add, commit

브랜치 안에서 push 할 때는 `git push -u origin {브랜치명}`

#### merge

나뉜 branch들을 하나로 합치는 명령어

`git merge {브랜치 명}`

병합 종류

- 

- 브랜치 합치기
  - master 브랜치 공간으로 이동
  - `git merge viktor`, 브랜치 명 입력해서 합침
  - `git log --oneline --graph` 치면 그림으로 이해 가능

Fast-forward



#### conflict

두 브랜치에서 같은 부분을 수정한 경우, 어느 브랜치 기준으로 작성해야 하는지 판단할 수 없어 충돌이 발생했을 때 해결하는 방법

보통 같은 파일의 같은 부분을 수정했을 때 발생



실습

- master 브랜치와 viktor 브랜치의 a.txt 첫줄에 각각 '난 마스터', '난 빅터' 입력

- 이후 `git merge master` 치면 경고 메시지 나옴

  ```
  Auto-merging a.txt
  CONFLICT (content): Merge conflict in a.txt
  Automatic merge failed; fix conflicts and then commit the result.
  ```

- 이후 a.txt 도 보면 아래처럼 저장되어있음

- ```
  <<<<<<< HEAD
  난 빅터
  =======
  난 마스터
  >>>>>>> master
  ```

- a.txt를 아래처럼 바꾸고 (원하는 형태로)

- ```
  난 빅터
  ```

  이렇게 하면 양쪽 가지의 a.txt 내용이 같아짐

- 바뀐 걸 add, commit





## Git workflow



원격 저장소 소유권이 있는 경우 => `Shared repository model`

원격 저장소 소유권이 없는 경우 => `Fork & Pull model`





#### Shared repository model

원격 저장소가 자신의 소유이거나 Collaborator로 등록되어 있는 경우

master 브랜치에 직접 개발하는 것이 아니라, 기능별로 브랜치를 따로 만들어 개발

`Pull Request`를 사용하여 팀원 간 변경 내용에 대한 소통 진행

실습

- 다른 사람들과 같이 하나의 pjt에 각자 브랜치 만들어서 브랜치에 push 한 뒤, merge
- 이후 git 홈페이지에서 merge 요청





#### Fork & Pull model

자신의 소유가 아닌 원격 저장소인 경우

원본 원격 저장소를 그대로 내 원격 저장소에 복제 (Fork)

기능 완성 후 복제한 내 원격 저장소에 push

이후 Pull Request를 통해 원본 원격 저장소에 반영될 수 있도록 요청함



실습

- 소유권이 없는 원격 저장소를 fork를 통해 내 원격 저장소로 복제
- 복제된 내 원격 저장소를 로컬 저장소에 clone
- 로컬 저장소, 원본 원격 저장소를 동기화 (`git remote add upstream {원본 url}`)
- 브랜치 생성, 코드 작성
- 복제 원격 저장소에 해당 브랜치 push
- Pull Request 요청
- 이후 사용자는 master로 switch, master에서 pull 해서 모두 같은 폴더 받기



