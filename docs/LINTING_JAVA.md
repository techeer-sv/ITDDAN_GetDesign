## Java 린팅 가이드

Java 코드의 스타일을 일관되게 유지하기 위한 Checkstyle 설정과 사용법을 안내합니다.

### 1. 도구 설치

```bash
wget -q https://github.com/checkstyle/checkstyle/releases/download/checkstyle-10.12.4/checkstyle-10.12.4-all.jar -O checkstyle.jar
````

> 위 명령어는 `checkstyle.jar` 파일이 없을 경우 한 번만 실행하면 됩니다.

### 2. 명령어

작성한 코드를 검사하고 스타일을 통일하는 방법입니다.

#### 코드 검사

`checkstyle.jar`와 `checkstyle.xml` 설정 파일을 사용하여 코드 스타일을 검사합니다.

```bash
java -jar checkstyle.jar -c checkstyle.xml <파일 경로>
```

예시:

```bash
java -jar checkstyle.jar -c checkstyle.xml FizzBuzz.java
```

> 참고: Java Checkstyle은 자동 수정 기능을 제공하지 않으므로, 검사 결과를 수동으로 반영해야 합니다.
