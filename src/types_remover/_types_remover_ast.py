import ast
from typing import Optional


class _DowngradeAnnAssign(ast.NodeTransformer):
	"""Converts AnnAssign nodes (annotated assignment) to simpler Assign nodes."""

	def visit_AnnAssign(self, node: ast.AnnAssign) -> Optional[ast.Assign]:
		if node.value is not None:
			return ast.Assign(targets = [node.target], value = node.value)
		return None  # just so mypy can leave me alone


def remove_types_ast(path: str, *, return_str: bool = False, output_file_path: Optional[str] = None) -> Optional[str]:
	"""
		Strips the types declared in the file at **path** and outputs it to output_file_path
		:param path: Required parameter deciding what file to strip from types
		:param return_str: dictates if the function returns a str
		:param output_file_path: dictates where the function saves the data
		:return: str if return_str is True else None
	"""
	if output_file_path is None:
		output_file_path = 'output.py'

	with open(path) as f:
		nodes = ast.parse(f.read())

	for node in ast.walk(nodes):
		if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
			# See: https://docs.python.org/3/library/ast.html#ast.arguments
			for arg in [*node.args.posonlyargs, *node.args.args, *node.args.kwonlyargs]:
				arg.annotation = None
			if node.args.vararg is not None:
				node.args.vararg.annotation = None
			if node.args.kwarg is not None:
				node.args.kwarg.annotation = None
			node.returns = None
	nodes = ast.fix_missing_locations(_DowngradeAnnAssign().visit(nodes))

	with open(output_file_path, 'w') as f:
		f.writelines(ast.unparse(nodes))
	if return_str:
		return ast.unparse(nodes)
	return None  # just so mypy can leave me alone
