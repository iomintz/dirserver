suffixes = ('KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB')

def natural_size(value, format='%.1f'):
	base = 1000
	bytes = float(value)

	if bytes < base: return '%d B' % bytes

	for i, s in enumerate(suffixes, 2):
		unit = base ** i
		if bytes < unit:
			return (format + ' %s') % ((base * bytes / unit), s)
	return (format + ' %s') % ((base * bytes / unit), s)

AUDIO_BYTES_NEEDED = 12

def mime_type_for_audio_data(data):
	if data[:4] == b'fLaC':
		return 'audio/flac'
	if data[:4] == b'RIFF' and data[8:12] == b'WAVE':
		return 'audio/basic'
	if data[:4] == b'FORM' and data[8:12] == b'AIFF':
		return 'audio/x-aiff'

data_is_opusenc_encodable = mime_type_for_audio_data

def mime_type_for_audio_path(f):
	with open(f, 'rb') as f:
		return mime_type_for_audio_data(f.read(AUDIO_BYTES_NEEDED))

path_is_opusenc_encodable = mime_type_for_audio_path
