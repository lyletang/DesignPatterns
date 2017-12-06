# -*- coding: utf-8 -*-
# author: lyletang
# date: 2017-12-06


from state_machine import State, Event, acts_as_state_machine,\
                          after, before, InvalidStateTransition


@acts_as_state_machine
class Process:
    """每个创建好的进程都有自己的状态机"""

    # 定义状态机的状态，状态机初始状态由initial指定
    created = State(initial=True)
    waiting = State()
    running = State()
    terminated = State()
    blocked = State()
    swapped_out_waiting = State()
    swapped_out_blocked = State()

    # 定义状态转换，在state_machine模块中，一个状态转换就是一个Event
    wait = Event(from_states=(created, running, blocked, swapped_out_waiting),
                 to_state=waiting)
    run = Event(from_states=waiting, to_state=running)
    terminate = Event(from_states=running, to_state=terminated)
    block = Event(from_states=(running, swapped_out_blocked),
                  to_state=blocked)
    swap_wait = Event(from_states=waiting, to_state=swapped_out_waiting)
    swap_block = Event(from_states=blocked, to_state=swapped_out_blocked)

    # 进程名
    def __init__(self, name):
        self.name = name

    # @before／@after用于在状态转换之前或之后执行动作
    @after('wait')
    def wait_info(self):
        print('{} entered waiting mode'.format(self.name))

    @after('run')
    def run_info(self):
        print('{} is running'.format(self.name))

    @before('terminate')
    def terminate_info(self):
        print('{} terminated'.format(self.name))

    @after('block')
    def block_info(self):
        print('{} is blocked'.format(self.name))

    @after('swap_wait')
    def swap_wait_info(self):
        print('{} is swapped out and waiting'.format(self.name))

    @after('swap_block')
    def swap_block_info(self):
        print('{} is swapped out and blocked'.format(self.name))


def transition(process, event, event_name):
    """尝试执行Event"""
    try:
        event()
    except InvalidStateTransition as err:
        print('Error: transition of {} from {} to {} failed'.format(
              process.name, process.current_state, event_name))


def state_info(process):
    """展示进程当前（激活）状态的一些信息"""
    print('state of {}: {}'.format(
          process.name, process.current_state))


def main():
    RUNNING = 'running'
    WAITING = 'waiting'
    BLOCKED = 'blocked'
    TERMINATED = 'terminated'

    p1, p2 = Process('process1'), Process('process2')
    [state_info(p) for p in (p1, p2)]

    print()
    transition(p1, p1.wait, WAITING)
    transition(p2, p2.terminate, TERMINATED)
    [state_info(p) for p in (p1, p2)]

    print()
    transition(p1, p1.run, RUNNING)
    transition(p2, p2.wait, WAITING)
    [state_info(p) for p in (p1, p2)]

    print()
    transition(p2, p2.run, RUNNING)
    [state_info(p) for p in (p1, p2)]

    print()
    [transition(p, p.block, BLOCKED) for p in (p1, p2)]
    [state_info(p) for p in (p1, p2)]

    print()
    [transition(p, p2.terminate, TERMINATED) for p in (p1, p2)]
    [state_info(p) for p in (p1, p2)]


if __name__ == '__main__':
    main()
