FULL = "pmoFDseSdfOMP"
CONCUR = "oFDseSdfO"

BASIC_COMPOSITION = {
('p', 'p'): 'p',
('m', 'p'): 'p',
('o', 'p'): 'p',
('F', 'p'): 'p',
('D', 'p'): 'p',
('s', 'p'): 'p',
('e', 'p'): 'p',
('S', 'p'): 'p',
('d', 'p'): 'pmosd',
('f', 'p'): 'pmosd',
('O', 'p'): 'pmosd',
('M', 'p'): 'pmosd',
('P', 'p'): FULL,
('p', 'm'): 'p',
('m', 'm'): 'p',
('o', 'm'): 'p',
('F', 'm'): 'p',
('D', 'm'): 'p',
('s', 'm'): 'm',
('e', 'm'): 'm',
('S', 'm'): 'm',
('d', 'm'): 'osd',
('f', 'm'): 'osd',
('O', 'm'): 'osd',
('M', 'm'): 'Fef',
('P', 'm'): 'DSOMP',
('p', 'o'): 'p',
('m', 'o'): 'p',
('o', 'o'): 'pmo',
('F', 'o'): 'pmo',
('D', 'o'): 'pmoFD',
('s', 'o'): 'o',
('e', 'o'): 'o',
('S', 'o'): 'oFD',
('d', 'o'): 'osd',
('f', 'o'): 'osd',
('O', 'o'): CONCUR,
('M', 'o'): 'DSO',
('P', 'o'): 'DSOMP',
('p', 'F'): 'p',
('m', 'F'): 'm',
('o', 'F'): 'o',
('F', 'F'): 'F',
('D', 'F'): 'D',
('s', 'F'): 'o',
('e', 'F'): 'F',
('S', 'F'): 'D',
('d', 'F'): 'osd',
('f', 'F'): 'Fef',
('O', 'F'): 'DSO',
('M', 'F'): 'DSO',
('P', 'F'): 'DSOMP',
('p', 'D'): 'pmoFD',
('m', 'D'): 'oFD',
('o', 'D'): 'oFD',
('F', 'D'): 'D',
('D', 'D'): 'D',
('s', 'D'): 'oFD',
('e', 'D'): 'D',
('S', 'D'): 'D',
('d', 'D'): CONCUR,
('f', 'D'): 'DSO',
('O', 'D'): 'DSO',
('M', 'D'): 'DSO',
('P', 'D'): 'DSOMP',
('p', 's'): 'p',
('m', 's'): 'p',
('o', 's'): 'pmo',
('F', 's'): 'pmo',
('D', 's'): 'pmoFD',
('s', 's'): 's',
('e', 's'): 's',
('S', 's'): 'seS',
('d', 's'): 'd',
('f', 's'): 'd',
('O', 's'): 'dfO',
('M', 's'): 'M',
('P', 's'): 'P',
('p', 'e'): 'p',
('m', 'e'): 'm',
('o', 'e'): 'o',
('F', 'e'): 'F',
('D', 'e'): 'D',
('s', 'e'): 's',
('e', 'e'): 'e',
('S', 'e'): 'S',
('d', 'e'): 'd',
('f', 'e'): 'f',
('O', 'e'): 'O',
('M', 'e'): 'M',
('P', 'e'): 'P',
('p', 'S'): 'pmoFD',
('m', 'S'): 'oFD',
('o', 'S'): 'oFD',
('F', 'S'): 'D',
('D', 'S'): 'D',
('s', 'S'): 'seS',
('e', 'S'): 'S',
('S', 'S'): 'S',
('d', 'S'): 'dfO',
('f', 'S'): 'O',
('O', 'S'): 'O',
('M', 'S'): 'M',
('P', 'S'): 'P',
('p', 'd'): 'p',
('m', 'd'): 'p',
('o', 'd'): 'pmosd',
('F', 'd'): 'pmosd',
('D', 'd'): FULL,
('s', 'd'): 'd',
('e', 'd'): 'd',
('S', 'd'): 'dfOMP',
('d', 'd'): 'd',
('f', 'd'): 'd',
('O', 'd'): 'dfOMP',
('M', 'd'): 'P',
('P', 'd'): 'P',
('p', 'f'): 'p',
('m', 'f'): 'm',
('o', 'f'): 'osd',
('F', 'f'): 'Fef',
('D', 'f'): 'DSOMP',
('s', 'f'): 'd',
('e', 'f'): 'f',
('S', 'f'): 'OMP',
('d', 'f'): 'd',
('f', 'f'): 'f',
('O', 'f'): 'OMP',
('M', 'f'): 'P',
('P', 'f'): 'P',
('p', 'O'): 'pmoFD',
('m', 'O'): 'oFD',
('o', 'O'): CONCUR,
('F', 'O'): 'DSO',
('D', 'O'): 'DSOMP',
('s', 'O'): 'dfO',
('e', 'O'): 'O',
('S', 'O'): 'OMP',
('d', 'O'): 'dfO',
('f', 'O'): 'O',
('O', 'O'): 'OMP',
('M', 'O'): 'P',
('P', 'O'): 'P',
('p', 'M'): 'pmoFD',
('m', 'M'): 'seS',
('o', 'M'): 'dfO',
('F', 'M'): 'M',
('D', 'M'): 'P',
('s', 'M'): 'dfO',
('e', 'M'): 'M',
('S', 'M'): 'P',
('d', 'M'): 'dfO',
('f', 'M'): 'M',
('O', 'M'): 'P',
('M', 'M'): 'P',
('P', 'M'): 'P',
('p', 'P'): FULL,
('m', 'P'): 'dfOMP',
('o', 'P'): 'dfOMP',
('F', 'P'): 'P',
('D', 'P'): 'P',
('s', 'P'): 'dfOMP',
('e', 'P'): 'P',
('S', 'P'): 'P',
('d', 'P'): 'dfOMP',
('f', 'P'): 'P',
('O', 'P'): 'P',
('M', 'P'): 'P',
('P', 'P'): 'P',
}
