#!/usr/bin/env python3
"""
简单的OpenClaw成本分析器
"""

import json
import os
import subprocess
from datetime import datetime, timedelta

def get_openclaw_logs():
    """获取OpenClaw日志路径"""
    log_paths = [
        "~/.openclaw/logs",
        "/var/log/openclaw",
        "/usr/local/var/log/openclaw"
    ]
    
    for path in log_paths:
        expanded = os.path.expanduser(path)
        if os.path.exists(expanded):
            return expanded
    return None

def analyze_recent_usage(days=7):
    """分析最近的使用情况"""
    print("🔍 OpenClaw 使用成本分析")
    print("=" * 50)
    
    # 检查会话
    try:
        result = subprocess.run(["openclaw", "sessions", "list", "--json"], 
                              capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            sessions = json.loads(result.stdout)
            print(f"📊 当前会话数: {len(sessions)}")
            
            # 分析最近活跃的会话
            active_sessions = [s for s in sessions if s.get('active', False)]
            print(f"📈 活跃会话: {len(active_sessions)}")
    except:
        pass
    
    # 检查模型使用
    print("\n🤖 模型使用统计:")
    print("  - DeepSeek Chat: 主要模型")
    print("  - 成本估算: 约 $0.14/1M tokens")
    
    # 建议
    print("\n💡 成本优化建议:")
    print("  1. 使用心跳(heartbeat)代替持续会话")
    print("  2. 对于长任务，使用子代理(subagents)")
    print("  3. 定期清理不用的会话")
    print("  4. 监控 memory/ 目录大小")
    
    # 检查文件大小
    workspace = os.path.expanduser("~/.openclaw/workspace")
    if os.path.exists(workspace):
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(workspace):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                total_size += os.path.getsize(fp)
        
        print(f"\n💾 工作空间大小: {total_size / 1024 / 1024:.2f} MB")
    
    print("\n📅 分析时间:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

if __name__ == "__main__":
    analyze_recent_usage()