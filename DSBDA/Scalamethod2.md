```
import scala.io.StdIn
object AddTwoNumbers {
def main(args: Array[String]): Unit = {
println("Enter the first number:")
val num1 = StdIn.readInt()
println("Enter the second number:")
val num2 = StdIn.readInt()
val sum = num1 + num2
println(s"The sum of $num1 and $num2 is $sum")
}
}
```
Save above program as demo.scala at any location (e.g.home or Desktop or Documents)
Now open the terminal and write following commands
mescoe@mescoe-Lenovo-S510:~$ `start-master.sh`
mescoe@mescoe-Lenovo-S510:~$ `source ~/.bashrc`
mescoe@mescoe-Lenovo-S510:~$ `spark-shell`
scala> `:load /home/mescoe/Documents/demo.scala`
Loading /home/mescoe/Documents/demo.scala...
import scala.io.StdIn
defined object AddTwoNumbers
scala> `AddTwoNumbers.main(Array.empty[String])`
o/p:
```
Enter the first number:
Enter the second number:
The sum of 15 and 25 is 40
```