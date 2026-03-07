Size*3, eyeSize/2, 0, Math.PI * 2);
                        ctx.fill();
                    } else if (direction.x === -1) {
                        ctx.beginPath();
                        ctx.arc(x + eyeSize*2, y + eyeSize*2, eyeSize/2, 0, Math.PI * 2);
                        ctx.fill();
                        ctx.beginPath();
                        ctx.arc(x + eyeSize*2, y + GRID_SIZE - eyeSize*3, eyeSize/2, 0, Math.PI * 2);
                        ctx.fill();
                    } else if (direction.y === -1) {
                        ctx.beginPath();
                        ctx.arc(x + eyeSize*2, y + eyeSize*2, eyeSize/2, 0, Math.PI * 2);
                        ctx.fill();
                        ctx.beginPath();
                        ctx.arc(x + GRID_SIZE - eyeSize*3, y + eyeSize*2, eyeSize/2, 0, Math.PI * 2);
                        ctx.fill();
                    } else {
                        ctx.beginPath();
                        ctx.arc(x + eyeSize*2, y + GRID_SIZE - eyeSize*2, eyeSize/2, 0, Math.PI * 2);
                        ctx.fill();
                        ctx.beginPath();
                        ctx.arc(x + GRID_SIZE - eyeSize*3, y + GRID_SIZE - eyeSize*2, eyeSize/2, 0, Math.PI * 2);
                        ctx.fill();
                    }
                }
            });
            
            // 绘制食物
            ctx.fillStyle = '#ff4757';
            const foodX = food.x * GRID_SIZE;
            const foodY = food.y * GRID_SIZE;
            ctx.beginPath();
            ctx.arc(foodX + GRID_SIZE/2, foodY + GRID_SIZE/2, GRID_SIZE/2 - 2, 0, Math.PI * 2);
            ctx.fill();
            
            // 食物细节
            ctx.fillStyle = '#ff6b81';
            ctx.beginPath();
            ctx.arc(foodX + GRID_SIZE/2, foodY + GRID_SIZE/2, GRID_SIZE/4, 0, Math.PI * 2);
            ctx.fill();
            
            requestAnimationFrame(draw);
        }

        // 改变方向
        function changeDirection(dir) {
            if (gameOver || isPaused) return;
            
            switch(dir) {
                case 'up':
                    if (direction.y !== 1) nextDirection = { x: 0, y: -1 };
                    break;
                case 'down':
                    if (direction.y !== -1) nextDirection = { x: 0, y: 1 };
                    break;
                case 'left':
                    if (direction.x !== 1) nextDirection = { x: -1, y: 0 };
                    break;
                case 'right':
                    if (direction.x !== -1) nextDirection = { x: 1, y: 0 };
                    break;
            }
        }

        // 键盘控制
        function handleKeyPress(event) {
            if (gameOver || isPaused) return;
            
            switch(event.key) {
                case 'ArrowUp':
                case 'w':
                case 'W':
                    if (direction.y !== 1) nextDirection = { x: 0, y: -1 };
                    event.preventDefault();
                    break;
                case 'ArrowDown':
                case 's':
                case 'S':
                    if (direction.y !== -1) nextDirection = { x: 0, y: 1 };
                    event.preventDefault();
                    break;
                case 'ArrowLeft':
                case 'a':
                case 'A':
                    if (direction.x !== 1) nextDirection = { x: -1, y: 0 };
                    event.preventDefault();
                    break;
                case 'ArrowRight':
                case 'd':
                case 'D':
                    if (direction.x !== -1) nextDirection = { x: 1, y: 0 };
                    event.preventDefault();
                    break;
            }
        }

        // 开始游戏
        function startGame() {
            if (isRunning) return;
            
            isRunning = true;
            isPaused = false;
            gameOver = false;
            
            document.getElementById('startBtn').disabled = true;
            document.getElementById('pauseBtn').disabled = false;
            
            gameLoop = setInterval(update, speed);
        }

        // 切换暂停
        function togglePause() {
            if (gameOver) return;
            
            isPaused = !isPaused;
            document.getElementById('pauseBtn').textContent = isPaused ? '继续' : '暂停';
        }

        // 重新开始游戏
        function restartGame() {
            clearInterval(gameLoop);
            resetGame();
            startGame();
        }

        // 游戏结束
        function endGame() {
            gameOver = true;
            isRunning = false;
            clearInterval(gameLoop);
            
            // 更新最高分
            if (score > highScore) {
                highScore = score;
                localStorage.setItem(HIGH_SCORE_KEY, highScore);
                updateHighScoreDisplay();
            }
            
            // 显示游戏结束画面
            document.getElementById('finalScore').textContent = score;
            document.getElementById('gameOverScreen').style.display = 'flex';
            
            document.getElementById('startBtn').disabled = false;
            document.getElementById('pauseBtn').disabled = true;
        }

        // 更新显示
        function updateDisplay() {
            document.getElementById('score').textContent = score;
            document.getElementById('length').textContent = snake.length;
            document.getElementById('speed').textContent = Math.floor(1000 / speed);
        }

        // 更新最高分显示
        function updateHighScoreDisplay() {
            // 可以在页面上添加最高分显示
            const highScoreElement = document.getElementById('highScore');
            if (highScoreElement) {
                highScoreElement.textContent = highScore;
            }
        }

        // 页面加载完成后初始化
        window.onload = function() {
            initGame();
            // 添加最高分显示
            const stats = document.querySelector('.stats');
            const highScoreItem = document.createElement('div');
            highScoreItem.className = 'stat-item';
            highScoreItem.innerHTML = `
                <div class="stat-value" id="highScore">${highScore}</div>
                <div class="stat-label">最高分</div>
            `;
            stats.appendChild(highScoreItem);
        };

        // 防止页面滚动
        document.addEventListener('touchmove', function(e) {
            if (e.target.classList.contains('control-btn') || 
                e.target.classList.contains('action-btn')) {
                e.preventDefault();
            }
        }, { passive: false });

        // 响应式调整
        window.addEventListener('resize', function() {
            const container = document.querySelector('.game-container');
            const size = Math.min(container.clientWidth, container.clientHeight);
            canvas.width = size;
            canvas.height = size;
            gridWidth = Math.floor(canvas.width / GRID_SIZE);
            gridHeight = Math.floor(canvas.height / GRID_SIZE);
            draw();
        });