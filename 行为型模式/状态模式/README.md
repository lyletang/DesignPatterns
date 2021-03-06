# 状态模式

面向对象编程着力于对象交互时改变它们的状态。在很多问题中，有限状态机（通常名为状态机）是一个非常方便的状态转换建模工具。首先，什么是状态机？状态机是一个抽象机器，有两个关键部分，状态和转换。状态是指系统的当前（激活）状况。例如，假设我们有一个收音机，其两个可能的状态是在调频波段（FM）或调幅波段（AM）上调节。另一个可能的状态是从一个FM／AM无线电台切换到另一个。转化是指从一个状态切换到另一个状态，因某个事件或条件的触发而开始。通常，在一次转换发生之前或之后回执行一个或一组动作。假设我们的收音机被调到107FM无限电台，一次状态转换的例子就是收听人按下按钮切换到107.5FM。

状态机可用于解决多种不同的问题，包括非计算机的问题。非计算机的例子包括自动售货机、电梯、交通灯等。计算机方面的例子包括游戏编程和计算编程的其他领域、硬件设计、协议设计，以及编程语言解析和网页。

其实，状态模式就是应用到一个特定软件工程问题的状态机。

`Summary`

状态模式，是一个或多个有限状态机（简称状态机）的实现，用于解决一个特定的软件工程问题。

状态机，是一个抽象机器，具有两个主要部分：状态和转换。状态是指一个系统的当前状态，一个状态机在任何时间点只有一个激活状态。转换是指从当前状态到一个新状态的切换。在一个转换发生之前或之后通常会执行一个或多个动作。状态机可以使用状态图进行视觉上的展现。
