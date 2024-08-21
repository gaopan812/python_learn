from fractions import Fraction
import re

print(
    len(
        set(
            map(
                lambda expr: eval(
                    re.sub(r'([\d.]+)', r'Fraction("\1")', expr)
                ),
                filter(
                    lambda s: not s.endswith('/0'),
                    (
                        ''.join(
                            str(j) + ('', '+', '-', '*', '/')[i // 5 ** (j - 1) % 5]
                            for j in range(1, 10)
                        ) + '0'
                        for i in range(1, 5 ** 9)
                    )
                )
            )
        )
    )
)
