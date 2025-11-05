@ pytest.mark.params([('0',nep point),
                      ('10',Unsuccessful),
                      ('12',Good),
                      ('14',Very good),
                      ('16',Excellent),
                      ('20',Very Excellent)])

def test_exam_total_points(point->int ,return->string,expected_total):
    actnal_total = exam_point( point,expected_total)
    assert actnal_total == expected_total

