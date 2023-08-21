# 这是一个用来分析py文件内部变量 方法 参数的模块
import ast


def extract_variables(node):
    variables = []
    if isinstance(node, ast.Assign):
        for target in node.targets:
            if isinstance(target, ast.Name):
                variables.append(target.id)
    return variables


def extract_functions(node):
    functions = []
    if isinstance(node, ast.FunctionDef):
        functions.append(node.name)
    return functions


def extract_parameters(node):
    parameters = []
    if isinstance(node, ast.FunctionDef):
        parameters.extend([arg.arg for arg in node.args.args])
    return parameters


def analyze_file(filename):
    with open(filename, "r") as file:
        source_code = file.read()
        tree = ast.parse(source_code)

        variables = []
        functions = []
        parameters = []

        for node in ast.walk(tree):
            variables.extend(extract_variables(node))
            functions.extend(extract_functions(node))
            parameters.extend(extract_parameters(node))

        return variables, functions, parameters
