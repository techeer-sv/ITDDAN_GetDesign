package jungeun.week12;

public class FindKim {
    public String solution(String[] seoul) {
        for (int i = 0; i < seoul.length; i++) {
            if (seoul[i].equals("Kim")) {
                return "김서방은 " + i + "에 있다";
            }
        }
        return "";
    }

    public static void main(String[] args) {
        FindKim findKim = new FindKim();

        // 테스트 케이스 1
        String[] seoul1 = { "Jane", "Kim" };
        System.out.println(findKim.solution(seoul1));

        // 테스트 케이스 2
        String[] seoul2 = { "Kim", "Park", "Lee" };
        System.out.println(findKim.solution(seoul2));
    }
}
