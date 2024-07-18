- git add 시 modified content, untracked content라고 메세지가 나타나며 add가 안됨
- 해당 파일 vscode 실행 시 The editor could not be opened due to an unexpected error: Unable to read file이란 메세지가 나타나며 파일을 열 수 없음

- 해결방법
```
제대로 추가되지 않던 폴더의 .git 폴더를 제거
git rm -rf --cached/해당폴더         #git cache 제거
git add 해당폴더                     #정상작동
```