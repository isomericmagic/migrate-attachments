select attachment.title as "Attachment Name", 
page.title as "Page Title", 
spaces.spacekey as "Space Key",
spaces.spaceid as "Space ID",
page.contentid as "Page ID",
attachment.contentid as "Attachment ID"
from content attachment
inner join content page on attachment.pageid = page.contentid
inner join spaces on attachment.spaceid = spaces.spaceid
where attachment.contenttype = 'ATTACHMENT' and attachment.prevver is null and spaces.spacekey = '<insert spacekey here>'

