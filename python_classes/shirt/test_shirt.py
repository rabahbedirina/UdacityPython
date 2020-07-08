import shirt as st

assert st.shirt_one.color == 'red', ' shirt_one should be red'
assert st.shirt_one.price == 10, 'shirt_one price should be 10'
assert st.shirt_one.style == 'long-sleeve', 'shirt_one should be long_sleeve style'
assert st.shirt_one.size == 'S', 'shirt_one size should be S'

assert st.shirt_two.price == 10, 'shirt_two price should be 10'
assert st.shirt_two.color == 'orange', 'shirt_two should be orange'
assert st.shirt_two.style == 'short-sleeve', 'shirt_two should be short_sleeve style'
assert st.shirt_two.size == 'L', 'shirt_two size should be L'

assert st.total == 20, 'the total_cost of both shirts should be 20'

assert round(st.total_discount) == 18, 'total_discount should be 18.0'