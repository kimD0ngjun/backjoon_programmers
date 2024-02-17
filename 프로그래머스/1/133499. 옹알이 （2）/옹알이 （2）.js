function solution(babbling) {
    // 카운팅용 변수
    let answer = 0;
    
    // 중복 문자열 필터링용
    const str = ["aya", "ye", "woo", "ma"];
    const repeatStr = ["ayaaya", "yeye", "woowoo", "mama"];
    
    for (let i = 0; i < babbling.length; i++) {
        // repeatStr에 해당하면 "R"로 대체
        // (대체 후에 혹은 그냥 지나치고) 남은 문자열 공백으로 대체
        for (let j = 0; j < str.length; j++) {
            babbling[i] = 
                babbling[i].replaceAll(repeatStr[j], "R")
                .replaceAll(str[j], " ");
        }
        
        // 공백만 남으면 trim()하면 길이 0됨
        // 반복되지 않는 스트링이니 발음 쌉가능
        // 카운팅
        if (babbling[i].trim().length == 0) {
            answer++;
        }
    }
    // 최종 결과 반환
    return answer;
}