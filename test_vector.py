import unittest
from vector import Vector
from decimal import Decimal

class TestVectorBasicOps(unittest.TestCase):
    def test_scalar(self):        
        v1 = Vector([1.671, -1.012, -0.318])
        v2 = v1.times_scalar(7.41)        
        scaledVec = Vector([12.382, -7.499,-2.356])
        for val1,val2 in zip(v2.coordinates, scaledVec.coordinates):
            self.assertAlmostEqual(val1,val2, 3)

    def test_plus(self):
        v1 = Vector([8.218,-9.341])
        v2 = Vector([-1.129, 2.111])
        result = v1.plus(v2)
        vplus = Vector([7.089, -7.230])
        for val1, val2 in zip(vplus.coordinates, result.coordinates):
            self.assertAlmostEqual(val1,val2,3)

    def test_minus(self):
        v1 = Vector([7.119, 8.215])
        v2 = Vector([-8.223, 0.878])        
        result = v1.minus(v2)
        vminus = Vector([15.342, 7.337])
        for val1, val2 in zip(vminus.coordinates, result.coordinates):
            self.assertAlmostEqual(val1,val2,3)

    def test_magnitude(self):
        v1 = Vector([-0.221, 7.437])
        v2 = Vector([8.813, -1.331, -6.247])
        vmag1 = v1.magnitude()
        vmag2 = v2.magnitude()
        vr1 = Decimal(7.440)
        vr2 = Decimal(10.884)
        self.assertAlmostEqual(vmag1, vr1, 3)
        self.assertAlmostEqual(vmag2, vr2, 3)

    def test_normalization(self):
        v1 = Vector([5.581, -2.136])
        v2 = Vector([1.996, 3.108, -4.554])
        v1norm = v1.normalized()
        v2norm = v2.normalized()
        vr1 = Vector([0.934, -0.357])
        vr2 = Vector([0.340, 0.530, -0.777])

        for val1, val2 in zip(v1norm.coordinates, vr1.coordinates):
            self.assertAlmostEqual(val1,val2, 3)

        for val1, val2 in zip(v2norm.coordinates, vr2.coordinates):
            self.assertAlmostEqual(val1,val2, 3)

        #assert vector 0 
        v0 = Vector([0,0])
        self.assertRaises(Exception,v0.normalized)

    def test_dot(self):
        v1 = Vector([7.887, 4.138])
        w1 = Vector([-8.802, 6.776])
        v2 = Vector([-5.955, -4.904, -1.874])
        w2 = Vector([-4.496, -8.755, 7.103])
        vdot1 = v1.dot(w1)
        vdot2 = v2.dot(w2)
        vr1 = Decimal(-41.382)
        vr2 = Decimal(56.397)
        
        self.assertAlmostEqual(vdot1,vr1, 3)
        self.assertAlmostEqual(vdot2,vr2, 3)
    
    def test_angle(self):
        v1 = Vector([3.183, -7.627])
        w1 = Vector([-2.668, 5.319])
        v2 = Vector([7.35, 0.221, 5.188])
        w2 = Vector([2.751, 8.259, 3.985])        
        vang1 = v1.angle(w1)
        vang2 = v2.angle(w2, in_degrees=True)
        vr1 = (3.072)
        vr2 = (60.276)
        self.assertAlmostEqual(vr1, vang1,3)
        self.assertAlmostEqual(vr2, vang2,3)
    
    def test_parallels(self):
        v1 = Vector([-7.579, -7.88])
        w1 = Vector([22.737, 23.64])

        v2 = Vector([-2.029, 9.97, 4.172])
        w2 = Vector([-9-231, -6.639, -7.245])

        v3 = Vector([-2.328, -7.284, -1.214])
        w3 = Vector([-1.821, 1.072, -2.94])

        v4 = Vector([2.118, 4.827])
        w4 = Vector([0,0])

        self.assertEqual(v1.is_parallel_to(w1), True)
        self.assertEqual(v2.is_parallel_to(w2), False)
        self.assertEqual(v3.is_parallel_to(w3), False)
        self.assertEqual(v4.is_parallel_to(w4), True)

    def test_orthogonals(self):
        v1 = Vector([-7.579, -7.88])
        w1 = Vector([22.737, 23.64])

        v2 = Vector([-2.029, 9.97, 4.172])
        w2 = Vector([-9-231, -6.639, -7.245])

        v3 = Vector([-2.328, -7.284, -1.214])
        w3 = Vector([-1.821, 1.072, -2.94])

        v4 = Vector([2.118, 4.827])
        w4 = Vector([0,0])

        self.assertEqual(v1.is_ortoghonal_to(w1), False)
        self.assertEqual(v2.is_ortoghonal_to(w2), False)
        self.assertEqual(v3.is_ortoghonal_to(w3), True)
        self.assertEqual(v4.is_ortoghonal_to(w4), True)

    

            

        
        
