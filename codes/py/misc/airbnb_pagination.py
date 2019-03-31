def paginate(num, results):
   if not results:
       return []

   skip = set()
   res = []
   idx = 0
   while idx < len(results):
       dedup = set()
       next_idx = None
       count = 0
       for i in range(idx, len(results)):
           if i in skip: continue
           (host_id, listing_id, score, name) = results[i].split(',')
           if host_id in dedup:
               if next_idx is None:
                   next_idx = i
           else:
               skip.add(i)
               dedup.add(host_id)
               res.append(results[i])
               count += 1
               if count == num:
                   break
       if next_idx is None:
           next_idx = i + 1
       idx = next_idx

       while idx < len(results) and count < num:
           if idx in skip:
               idx += 1
               continue
           skip.add(idx)
           res.append(results[idx])
           count += 1
           idx += 1
       res.append('')

   if res[-1] == '':
       res.pop()
   return res
