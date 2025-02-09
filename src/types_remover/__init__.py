from typing import Optional, Literal

from ._types_remover_ast import remove_types_ast as remove_types_ast
from ._types_remover_if import remove_types as remove_types_if


__all__ = ['remove_types','remove_types_if', 'remove_types_ast']
__author__ = 'EasternFarmer'


def remove_types(
    path: str,
    *,
    implementation: Literal['ast', 'if'] = 'ast',
    return_str: bool = False,
    output_file_path: Optional[str] = None
    ) -> Optional[str]:

    if implementation == 'ast':
        return remove_types_ast(
            path,
            return_str = return_str,
            output_file_path = output_file_path
            )
    elif implementation == 'if':
        return remove_types_if(
            path,
            return_str = return_str,
            output_file_path = output_file_path
            )
    else:
        raise ValueError('Invalid implementation specified.')