import random
from reprowd.crowdcontext import *
from reprowd.presenter.image import ImageCmp

# credit to https://github.com/sfu-db/reprowd/blob/master/reprowd/examples/quicksort.py
def _quicksort(crowddata, object_list, orig_img):
    if len(object_list) <= 1:
        return crowddata

    pivot_index = random.randint(0, len(object_list)-1)
    pivot = object_list.pop(pivot_index)

    object_pair_list = [(orig_img, o, pivot) for o in object_list]
    crowddata = crowddata.clear().extend(object_pair_list).publish_task().get_result().quality_control("mv")

    left = []
    right = []
    for obj, result in zip(crowddata.data['object'], crowddata.data['mv']):
        if result == 'right':
            left.append(obj[1])
        else:
            right.append(obj[1])

    crowddata = _quicksort(crowddata, left, orig_img)
    crowddata = _quicksort(crowddata, right, orig_img)
    object_list[:] = left+[pivot]+right

    return crowddata

# customized for using an original with comparisons for quicksort list 
def quicksort(object_list, table_name, custom_presenter, custom_map_func, orig_img, seed, cc):
    random.seed(seed)  # This is to gaurantee that quicksort is determinintic.
    crowddata = cc.CrowdData([], table_name = table_name) \
                            .set_presenter(custom_presenter, custom_map_func)
    _quicksort(crowddata, object_list, orig_img)


if __name__ == "__main__":
    cc = CrowdContext()

    object_list = ["http://www.kidsmathgamesonline.com/images/pictures/numbers600/number3.jpg",
            "http://www.kidsmathgamesonline.com/images/pictures/numbers600/number4.jpg",
            "http://www.kidsmathgamesonline.com/images/pictures/numbers600/number2.jpg",
            "http://www.kidsmathgamesonline.com/images/pictures/numbers600/number1.jpg",
            "http://www.kidsmathgamesonline.com/images/pictures/numbers600/number5.jpg"]

    cc.delete_table("quicksort")
    print "Unsorted Data:"
    print "\n".join(object_list)

    quicksort(object_list, "quicksort", 1, cc)

    print "Sorted Data:"
    print "\n".join(object_list)
