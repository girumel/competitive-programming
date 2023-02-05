class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        top = -1
        for operation in operations:
            if (operation.strip('-')).isnumeric():
                record.append(int(operation))
                top += 1
            elif operation == '+' and len(record) > 1:
                record.append(sum(record[top - 1:top + 2]))
                top += 1
            elif operation == 'D':
                record.append(2 * record[top])
                top += 1
            elif operation == 'C':
                record.pop(top)
                top -= 1
        return sum(record)
        