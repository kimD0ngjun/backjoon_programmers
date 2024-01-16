import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        Map<String, Integer> participantMap = new HashMap<>();
        
        for (String player : participant) {
            participantMap.put(player, 
                               participantMap.getOrDefault(player, 0) + 1);
        }
        
        for (String player : completion) {
            participantMap.put(player, participantMap.get(player) - 1);
        }
        
        for (Map.Entry<String, Integer> entry : participantMap.entrySet()) {
            if (entry.getValue() == 1) {
                return entry.getKey();
            }
        }
        
        return null;
    }
}