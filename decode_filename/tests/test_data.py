from decode_filename.data import decode_filename

def test_decode_filename:
	SampleGoodFileNames = ('BJ9909.pdf','BJ1709.pdf','SUNY071031.pdf')
	SampleBadFileNames = ('.DS_Store','Ben07Q3.pdf','401K1710.pdf')
	for f in SampleGoodFileNames:
    	assert decode_filename(f) > 0.0
    for f in SampleBadFileNames:
    	assert decode_filename(f) < 0.1
