def prod_signs(arr):
    if not arr:
        return None
    
    def compute_sum_magnitudes(nums):
        return sum(abs(num) for num in nums)
    
    def compute_sign_product(nums):
        try:
            import signutils
            signs = [signutils.get_sign(num) for num in nums]
        except ImportError:
            signs = []
            for num in nums:
                if num > 0:
                    signs.append(1)
                elif num < 0:
                    signs.append(-1)
                else:
                    signs.append(0)
        return prod_signs(signs)
    
    magnitude_sum = compute_sum_magnitudes(arr)
    sign_product = compute_sign_product(arr)
    
    return magnitude_sum * sign_product if sign_product is not None else 0