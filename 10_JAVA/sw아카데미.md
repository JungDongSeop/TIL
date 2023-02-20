숫자 읽기

```java
import java.io.FileInputStream;
import java.util.Arrays;
import java.util.Scanner;

public class Solution {
    public static void main(String args[]) throws Exception
    {
        System.setIn(new FileInputStream("res/input.txt"));

//      전체 입력
        Scanner sc = new Scanner(System.in);
        // 테케 숫자 입력
        int testCase = sc.nextInt();

        // 테케 반복문
        for(int tc=1; tc<=10; tc++) {
            // 첫 숫자 입력
            int t = sc.nextInt();
            // 행렬 선언
            int[] arr = new int[1000];

//            행렬에서 입력받기
            for(int i = 0; i < 1000; i++) {
                arr[i] = sc.nextInt();
            }

            ....코드 작성

            // 정답 출력
            System.out.printf("#%d %d\n", tc, answer);
        }
    }
}

```



