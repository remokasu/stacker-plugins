from __future__ import annotations

from stacker.stacker import Stacker


def tolist(stacker, start, end):
    sublist = stacker.stack[start:end]
    new_stack = (stacker.stack[:start] + [sublist] + stacker.stack[end:])
    stacker.stack = new_stack


def unlist(stacker, index: int) -> None:
    if not stacker.stack:
        raise ValueError("Stack is empty")
    if index < 0 or index >= len(stacker.stack):
        raise IndexError("Invalid index")

    target = stacker.stack[index]
    if not isinstance(target, list):
        raise TypeError("Target element is not a list")

    stacker.stack = stacker.stack[:index] + target + stacker.stack[index + 1 :]


def setup(stacker: Stacker):
    stacker.register_plugin(
        "tolist",
        tolist,
        push_result_to_stack=False,
        pass_core=True,
        description_en="Convert a specified range within the stack into a single list element",
        description_jp="スタック内の指定された範囲を1つのリスト要素に変換する",
    )
    stacker.register_plugin(
        operator_name="unlist",
        operator_func=unlist,
        push_result_to_stack=False,
        pass_core=True,
        description_en="Expand the list at the specified index of the stack",
        description_jp="スタックの指定されたインデックスにあるリストを展開する",
    )
