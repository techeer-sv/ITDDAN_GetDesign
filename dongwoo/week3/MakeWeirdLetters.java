package dongwoo.week3;

public class MakeWeirdLetters {
    /**
     * 문자열 s를 JadenCase 형식으로 변환한다.
     * 각 단어의 짝수 인덱스 문자는 대문자, 홀수 인덱스 문자는 소문자로 변환한다.
     */
    public static String makeWeirdLetters(String s) {
        StringBuilder answer = new StringBuilder();
        String[] words = s.split(" ", -1); // 공백 유지 split

        for (int i = 0; i < words.length; i++) {
            String word = words[i];
            StringBuilder temp = new StringBuilder();

            for (int j = 0; j < word.length(); j++) {
                char ch = word.charAt(j);
                if (j % 2 == 0) {
                    temp.append(Character.toUpperCase(ch));
                } else {
                    temp.append(Character.toLowerCase(ch));
                }
            }

            answer.append(temp);
            if (i != words.length - 1) {
                answer.append(" ");
            }
        }

        return answer.toString();
    }

    /**
     * 테스트 메서드
     */
    public static void testMakeWeirdLettersCase() {
        // 테스트 1
        String input1 = "try hello world";
        String expected1 = "TrY HeLlO WoRlD";
        String result1 = makeWeirdLetters(input1);
        System.out.println("Test 1 result: " + result1);
        assert result1.equals(expected1) : "Expected \"" + expected1 + "\", got \"" + result1 + "\"";

        // 테스트 2: 공백 포함
        String input2 = "  hello   world ";
        String expected2 = "  HeLlO   WoRlD ";
        String result2 = makeWeirdLetters(input2);
        System.out.println("Test 2 result: " + result2);
        assert result2.equals(expected2) : "Expected \"" + expected2 + "\", got \"" + result2 + "\"";

        // 테스트 3: 빈 문자열
        String input3 = "";
        String expected3 = "";
        String result3 = makeWeirdLetters(input3);
        System.out.println("Test 3 result: \"" + result3 + "\"");
        assert result3.equals(expected3) : "Expected \"" + expected3 + "\", got \"" + result3 + "\"";

        // 테스트 4: 숫자 포함
        String input4 = "a1 b2";
        String expected4 = "A1 B2";
        String result4 = makeWeirdLetters(input4);
        System.out.println("Test 4 result: " + result4);
        assert result4.equals(expected4) : "Expected \"" + expected4 + "\", got \"" + result4 + "\"";

        // 테스트 5: 한 글자 단어들
        String input5 = "a b c";
        String expected5 = "A B C";
        String result5 = makeWeirdLetters(input5);
        System.out.println("Test 5 result: " + result5);
        assert result5.equals(expected5) : "Expected \"" + expected5 + "\", got \"" + result5 + "\"";

        System.out.println("All tests passed for JadenCaseConverter!");
    }

    public static void main(String[] args) {
        testMakeWeirdLettersCase();
    }
}
