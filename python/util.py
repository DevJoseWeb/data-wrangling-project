def logging_itr(itr, step=500000):
    for i, x in enumerate(itr, 1):
        if i % step == 0:
            print 'Finished {} items'.format(i)
        yield x
