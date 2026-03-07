#!/usr/bin/env python3
"""
终端版贪吃蛇游戏 - 芋头🐱为你编写
使用WASD键控制，在终端中运行
"""

import os
import sys
import tty
import termios
import time
import random

# 游戏常量
WIDTH = 20
HEIGHT = 15
EMPTY = '·'
SNAKE_HEAD = '●'
SNAKE_BODY = '○'
FOOD = '★'
WALL = '█'

class SnakeGame:
    def __init__(self):
        self.width = WIDTH
        self.height = HEIGHT
        self.reset()
    
    def reset(self):
        """重置游戏状态"""
        self.snake = [(self.width // 2, self.height // 2)]
        self.direction = (1, 0)  # 初始向右
        self.food = self.generate_food()
        self.score = 0
        self.game_over = False
        self.speed = 0.2  # 初始速度
    
    def generate_food(self):
        """生成食物位置"""
        while True:
            food = (random.randint(1, self.width - 2), 
                   random.randint(1, self.height - 2))
            if food not in self.snake:
                return food
    
    def getch(self):
        """获取单个字符输入（非阻塞）"""
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
    
    def draw(self):
        """绘制游戏界面"""
        os.system('clear' if os.name == 'posix' else 'cls')
        
        print("=" * 40)
        print("        芋头🐱的贪吃蛇游戏")
        print("=" * 40)
        print(f"分数: {self.score} | 长度: {len(self.snake)} | 速度: {1/self.speed:.1f}格/秒")
        print("控制: W(上) A(左) S(下) D(右) | Q(退出) | R(重新开始)")
        print("=" * 40)
        
        # 绘制游戏区域
        for y in range(self.height):
            row = []
            for x in range(self.width):
                if x == 0 or x == self.width - 1 or y == 0 or y == self.height - 1:
                    row.append(WALL)  # 墙壁
                elif (x, y) == self.snake[0]:
                    row.append(SNAKE_HEAD)  # 蛇头
                elif (x, y) in self.snake:
                    row.append(SNAKE_BODY)  # 蛇身
                elif (x, y) == self.food:
                    row.append(FOOD)  # 食物
                else:
                    row.append(EMPTY)  # 空地
            print(' '.join(row))
        
        print("=" * 40)
        
        if self.game_over:
            print("💀 游戏结束！")
            print(f"最终分数: {self.score}")
            print("按 R 重新开始，按 Q 退出")
    
    def update(self):
        """更新游戏状态"""
        if self.game_over:
            return
        
        # 移动蛇
        head_x, head_y = self.snake[0]
        dir_x, dir_y = self.direction
        new_head = (head_x + dir_x, head_y + dir_y)
        
        # 检查碰撞
        if (new_head[0] <= 0 or new_head[0] >= self.width - 1 or
            new_head[1] <= 0 or new_head[1] >= self.height - 1 or
            new_head in self.snake):
            self.game_over = True
            return
        
        # 移动蛇
        self.snake.insert(0, new_head)
        
        # 检查是否吃到食物
        if new_head == self.food:
            self.score += 10
            self.food = self.generate_food()
            # 每得50分加速一次
            if self.score % 50 == 0 and self.speed > 0.05:
                self.speed *= 0.9
        else:
            self.snake.pop()  # 如果没有吃到食物，移除尾部
    
    def handle_input(self):
        """处理用户输入"""
        try:
            ch = self.getch().lower()
            
            if ch == 'q':
                return 'quit'
            elif ch == 'r' and self.game_over:
                self.reset()
                return 'continue'
            elif not self.game_over:
                if ch == 'w' and self.direction != (0, 1):
                    self.direction = (0, -1)  # 上
                elif ch == 's' and self.direction != (0, -1):
                    self.direction = (0, 1)   # 下
                elif ch == 'a' and self.direction != (1, 0):
                    self.direction = (-1, 0)  # 左
                elif ch == 'd' and self.direction != (-1, 0):
                    self.direction = (1, 0)   # 右
            
            return 'continue'
        except:
            return 'continue'
    
    def run(self):
        """运行游戏主循环"""
        print("正在启动贪吃蛇游戏...")
        time.sleep(1)
        
        while True:
            self.draw()
            
            # 处理输入（非阻塞）
            start_time = time.time()
            while time.time() - start_time < self.speed:
                if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
                    result = self.handle_input()
                    if result == 'quit':
                        print("\n游戏结束！谢谢游玩！")
                        return
            
            self.update()

def main():
    """主函数"""
    try:
        game = SnakeGame()
        game.run()
    except KeyboardInterrupt:
        print("\n\n游戏被中断。")
    except Exception as e:
        print(f"\n发生错误: {e}")

if __name__ == "__main__":
    # 导入select模块（用于非阻塞输入）
    import select
    
    main()