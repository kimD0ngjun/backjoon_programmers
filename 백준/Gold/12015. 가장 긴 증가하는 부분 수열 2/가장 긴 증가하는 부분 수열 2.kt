fun main() {
    val strN: String? = readLine()
    val strA: String? = readLine()

    val N: Int = strN?.toInt() ?: return
    val A: List<Int> = strA?.split(" ")?.map { s -> s.toInt() } ?: return

    val memo: IntArray = IntArray(A.size) {0}
    var pointer: Int = 0

    for (el in A) {
        var low: Int = 0
        var high: Int = pointer - 1

        while (low <= high) {
            val mid: Int = (low + high) / 2

            if (memo[mid] < el) low = mid + 1
            else high = mid - 1
        }

        if (low >= pointer) {
            memo[pointer] = el
            pointer++
        } else {
            memo[low] = el
        }
    }

    println(pointer)
}