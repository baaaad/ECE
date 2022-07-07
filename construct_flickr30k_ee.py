import json
import csv
from argparse import ArgumentParser







def contruct_flickr30kee(data_path, save_path):

    csv_file = csv.reader(open(data_path, 'r'))

    pairid2dic_contra = {}
    pairid2dic_entail = {}

    contra_list = []
    ental_list = []

    for annotation in csv_file:
        if str(annotation[1]) == "pairID":
            print(annotation)
            continue
        dictionary = {}
        dictionary["image_id"] = int(annotation[2].split(".")[0])
        dictionary["hypothesis"] = str(annotation[3])
        dictionary["pairID"] = str(annotation[1])
        if str(annotation[4]) == "-":
            dictionary["labels"] = []
            continue
        else:
            dictionary["labels"] = [
                str(annotation[4])
            ]
        if str(annotation[4]) == "entailment":
            ental_list.append(str(annotation[1]))
            pairid2dic_entail[str(annotation[1])] = dictionary
        if str(annotation[4]) == "contradiction":
            contra_list.append(str(annotation[1]))
            pairid2dic_contra[str(annotation[1])] = dictionary


    items = []

    for i in range(len(ental_list)):
        dictionary1 = {}

        entail_id = ental_list[i]
        contra_ids = [ental_list[i][:-1] + 'c', ental_list[i][:-1] + 'n', ental_list[i][:-1] + 'e']
        for contra_id in contra_ids:
            if contra_id in pairid2dic_contra:
                dictionary1["image_id"] = pairid2dic_entail[entail_id]["image_id"]
                dictionary1["Ref-Cap"] = pairid2dic_contra[contra_id]["hypothesis"]
                dictionary1["GT-Cap"] = pairid2dic_entail[entail_id]["hypothesis"]
                items.append(dictionary1)


    with open(save_path, 'w') as wr:
        json.dump(items, wr)


def main():
    parser = ArgumentParser()
    parser.add_argument('--split', type=str, required=True)
    args = parser.parse_args()

    data_path = 'dataset/esnlive/esnlive_{}.json'.format(args.split)
    save_path = 'output/flickr30k_ee_{}.json'.format(args.split)

    print('*** Flickr30K-EE Construction Start! ***')
    contruct_flickr30kee(data_path, save_path)
    print('*** Flickr30K-EE Construction Done! ***')




if __name__ == '__main__':
    main()


