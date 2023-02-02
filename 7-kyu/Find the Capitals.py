def capital(capitals):
    return [f'The capital of {element.get("state") or element.get("country")} is {element.get("capital")}' for element in capitals]

# Another solution
# def capital(capitals):
#     answer = []
#     for element in capitals:
#         answer.append(f'The capital of {element.get("state") or element.get("country")} is {element.get("capital")}')
#     return answer
