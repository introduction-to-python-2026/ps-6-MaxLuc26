def create_codon_dict(file_path):
    amino_dict = {}
    for i in rows:
      stripped = i.strip()
      polished = stripped.split('\t')
      amino_dict[polished[0]] = polished[2]
    return amino_dict


