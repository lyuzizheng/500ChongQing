"""
问题配置文件
"""
from enum import Enum
from typing import Dict, Any, List, Optional

class QuestionType(Enum):
    SINGLE_CHOICE = "single_choice"
    MULTIPLE_CHOICE = "multiple_choice"
    NUMBER = "number"
    TEXT = "text"
    COMBINATION = "combination"

class ScoringRule(Enum):
    STATIC_WEIGHT = "static_weight"  # 静态权重
    REAL_TIME_RANK = "real_time_rank"  # 实时排名
    DISTANCE_SCORE = "distance_score"  # 距离评分
    MAJORITY_VOTE = "majority_vote"  # 众数投票
    COUNT_RANK = "count_rank"  # 计数排名
    DYNAMIC_YN = "dynamic_yn"  # 动态Y/N判定
    VOTE_RANK_STATIC = "vote_rank_static" # 投票排名（静态分数）

QUESTIONS: Dict[str, Dict[str, Any]] = {
    "f": {
        "id": "f",
        "label": "绕口令——是否出错",
        "type": QuestionType.SINGLE_CHOICE.value,
        "options": ["Y", "N"],
        "rule": ScoringRule.STATIC_WEIGHT.value,
        "weights": {"Y": 1, "N": -1}
    },
    "g": {
        "id": "g",
        "label": "迷宫打卡次数",
        "type": QuestionType.NUMBER.value,
        "rule": ScoringRule.REAL_TIME_RANK.value,
        "range": [0, 1],
        "input_type": "positive_integer"
    },
    "h1": {
        "id": "h1",
        "label": "切蛋糕 #1「区县」",
        "type": QuestionType.TEXT.value,
        "rule": ScoringRule.DISTANCE_SCORE.value,
        "range": [0, 1]
    },
    "h2": {
        "id": "h2",
        "label": "切蛋糕 #2「直辖」",
        "type": QuestionType.TEXT.value,
        "rule": ScoringRule.DISTANCE_SCORE.value,
        "range": [0, 1]
    },
    "h3": {
        "id": "h3",
        "label": "切蛋糕 #3「最重庆」",
        "type": QuestionType.SINGLE_CHOICE.value,
        "options": ["选项1", "选项2", "选项3", "选项4"],  # 需要替换为实际选项
        "rule": ScoringRule.MAJORITY_VOTE.value,
        "range": [0, 1]
    },
    "i": {
        "id": "i",
        "label": "乱劈柴柴 —— 说出重庆黑话/地名个数",
        "type": QuestionType.NUMBER.value,
        "rule": ScoringRule.COUNT_RANK.value,
        "range": [0, 1],
        "input_type": "count"
    },
    "j": {
        "id": "j",
        "label": "夜景图片（多选 1）",
        "type": QuestionType.SINGLE_CHOICE.value,
        "options": ["图片1", "图片2", "图片3", "图片4"],  # 需要替换为实际选项
        "rule": ScoringRule.MAJORITY_VOTE.value,
        "range": [0, 1]
    },
    "k": {
        "id": "k",
        "label": "「山火文」对应对象",
        "type": QuestionType.SINGLE_CHOICE.value,
        "options": ["选项1", "选项2", "选项3", "选项4"],  # 需要替换为实际选项
        "rule": ScoringRule.MAJORITY_VOTE.value,
        "range": [0, 1]
    },
    "l": {
        "id": "l",
        "label": "打腔混搭（共 5 配合）",
        "type": QuestionType.SINGLE_CHOICE.value,
        "options": ["Y", "N"],
        "rule": ScoringRule.DYNAMIC_YN.value,
        "range": [-1, 1]
    },
    "m": {
        "id": "m",
        "label": "火锅油碟（需给每个调料打标签）",
        "type": QuestionType.COMBINATION.value,
        "options": ["香菜", "蒜泥", "香油", "耗油", "小米椒", "葱花", "花生碎", "芝麻"],  # 示例调料
        "rule": ScoringRule.MAJORITY_VOTE.value,
        "range": [0, 1]
    },
    "n": {
        "id": "n",
        "label": "打麻将——胡牌番数",
        "type": QuestionType.NUMBER.value,
        "rule": ScoringRule.REAL_TIME_RANK.value,
        "range": [0, 1],
        "input_type": "positive_integer"
    },
    "o1": {
        "id": "o1",
        "label": "量身高：身高",
        "type": QuestionType.NUMBER.value,
        "rule": ScoringRule.DISTANCE_SCORE.value,
        "range": [0, 0.2],
        "input_type": "height_cm",
        "metric": "abs_diff_from_avg"
    },
    "o2": {
        "id": "o2",
        "label": "量身高：社保年限",
        "type": QuestionType.NUMBER.value,
        "rule": ScoringRule.REAL_TIME_RANK.value,
        "range": [0, 0.2],
        "input_type": "years"
    },
    "o3": {
        "id": "o3",
        "label": "量身高：今日在山城巷消费",
        "type": QuestionType.NUMBER.value,
        "rule": ScoringRule.REAL_TIME_RANK.value,
        "range": [0, 0.2],
        "input_type": "money"
    },
    "o4": {
        "id": "o4",
        "label": "量身高：2024 年带来的外地游客数",
        "type": QuestionType.NUMBER.value,
        "rule": ScoringRule.REAL_TIME_RANK.value,
        "range": [0, 0.2],
        "input_type": "count"
    },
    "o5": {
        "id": "o5",
        "label": "量身高：人生迄今带来的重庆户口数",
        "type": QuestionType.NUMBER.value,
        "rule": ScoringRule.REAL_TIME_RANK.value,
        "range": [0, 0.2],
        "input_type": "count"
    },
    "q1": {
        "id": "q1",
        "label": "你希望如何称呼",
        "type": QuestionType.TEXT.value
    },
    "q2": {
        "id": "q2",
        "label": "你的性别",
        "type": QuestionType.SINGLE_CHOICE.value,
        "options": ["男", "女"],
    },
    "p": {
        "id": "p",
        "label": "你的MBTI",
        "type": QuestionType.TEXT.value,
    },
    "a1": {
        "id": "a1",
        "label": "身份证号前三位是否为'500'",
        "type": QuestionType.SINGLE_CHOICE.value,
        "options": ["Y", "N"],
        "rule": ScoringRule.STATIC_WEIGHT.value,
        "weights": {"Y": 1, "N": -1}
    },
    "a2": {
        "id": "a2",
        "label": "出生年份是否在1997年后",
        "type": QuestionType.SINGLE_CHOICE.value,
        "options": ["Y", "N"],
        "rule": ScoringRule.STATIC_WEIGHT.value,
        "weights": {"Y": 1, "N": 0}
    },
    "b1": {
        "id": "b1",
        "label": "父母是否都来自重庆",
        "type": QuestionType.SINGLE_CHOICE.value,
        "options": ["YY", "YN", "NN"],
        "rule": ScoringRule.STATIC_WEIGHT.value,
        "weights": {"YY": 1, "YN": 0, "NN": -1}
    },
    "b2": {
        "id": "b2",
        "label": "（若父母来自重庆）是否都来自主城九区",
        "type": QuestionType.SINGLE_CHOICE.value,
        "options": ["YY", "YN", "NN"],
        "rule": ScoringRule.STATIC_WEIGHT.value,
        "weights": {"YY": 1, "YN": 0.5, "NN": 0}
    },
    "b3": {
        "id": "b3",
        "label": "（若父母一方来自重庆）重庆的一方是否来自主城九区",
        "type": QuestionType.SINGLE_CHOICE.value,
        "options": ["Y", "N"],
        "rule": ScoringRule.STATIC_WEIGHT.value,
        "weights": {"Y": 1, "N": 0.5}
    },
    "b4": {
        "id": "b4",
        "label": "（若父母一方来自重庆）非重庆的一方是否来自四川",
        "type": QuestionType.SINGLE_CHOICE.value,
        "options": ["Y", "N"],
        "rule": ScoringRule.STATIC_WEIGHT.value,
        "weights": {"Y": 0, "N": -0.5}
    },
    "b5": {
        "id": "b5",
        "label": "（若父母都不来自重庆）是否都来自四川",
        "type": QuestionType.SINGLE_CHOICE.value,
        "options": ["YY", "YN", "NN"],
        "rule": ScoringRule.STATIC_WEIGHT.value,
        "weights": {"YY": 0.5, "YN": 0, "NN": -1}
    },
    "c1": {
        "id": "c1",
        "label": "童年所在地是否在重庆",
        "type": QuestionType.SINGLE_CHOICE.value,
        "options": ["Y", "N"],
        "rule": ScoringRule.STATIC_WEIGHT.value,
        "weights": {"Y": 1, "N": -1}
    },
    "c2": {
        "id": "c2",
        "label": "常居地/久居地是否在重庆",
        "type": QuestionType.SINGLE_CHOICE.value,
        "options": ["Y", "N"],
        "rule": ScoringRule.STATIC_WEIGHT.value,
        "weights": {"Y": 1, "N": -1}
    },
    "c3": {
        "id": "c3",
        "label": "在重庆待的时长",
        "type": QuestionType.NUMBER.value,
        "rule": ScoringRule.REAL_TIME_RANK.value,
        "range": [0, 1],
        "input_type": "months"
    },
    "e": {
        "id": "e",
        "label": "重庆的中心",
        "type": QuestionType.TEXT.value,
        "rule": ScoringRule.DISTANCE_SCORE.value,
        "range": [0, 1]
    },
    "r": {
        "id": "r",
        "label": "为后面的观众选择最能代表重庆的游戏",
        "type": QuestionType.SINGLE_CHOICE.value,
        "options": ["打脏话牌", "火锅油碟", "打麻将", "量身高"],
        "rule": ScoringRule.VOTE_RANK_STATIC.value,
        "scores": [1, 0.75, 0.5, 0.25]
    }
} 