from jplaw.types import HttpType

API_VERSION = "/api/v3"
API_PATH = {
    "login" :                               { "method": HttpType.POST    , "path": "/user/login"                            },
    "getPost" :                             { "method": HttpType.GET     , "path": "/post"                                  },
    "getCommunity" :                        { "method": HttpType.GET     , "path": "/community"                             },
    "listCommunities" :                     { "method": HttpType.GET     , "path": "/community/list"                        },
    "getPosts" :                            { "method": HttpType.GET     , "path": "/post/list"                             },
    "createPost" :                          { "method": HttpType.POST    , "path": "/post"                                  },
    "editPost" :                            { "method": HttpType.PUT     , "path": "/post"                                  },
    "createComment" :                       { "method": HttpType.POST    , "path": "/comment"                               },
    "likePost" :                            { "method": HttpType.POST    , "path": "/post/like"                             },
    "likeComment" :                         { "method": HttpType.POST    , "path": "/comment/like"                          },
    "followCommunity" :                     { "method": HttpType.POST    , "path": "/community/follow"                      },
    "resolveObject":                        { "method": HttpType.GET     , "path": "/resolve_object"                        },
    "search":                               { "method": HttpType.GET     , "path": "/search"                                },
    "getSite":                              { "method": HttpType.GET     , "path": "/site"                                  },
    "leaveAdmin":                           { "method": HttpType.POST    , "path": "/user/leave_admin"                      },
    "register":                             { "method": HttpType.POST    , "path": "/user/register"                         },
    "getPersonDetails":                     { "method": HttpType.GET     , "path": "/user"                                  },
    "getPersonMentions":                    { "method": HttpType.GET     , "path": "/user/mention"                          },
    "markPersonMentionAsRead":              { "method": HttpType.POST    , "path": "/user/mention/mark_as_read"             },
    "getReplies":                           { "method": HttpType.GET     , "path": "/user/replies"                          },
    "banPerson":                            { "method": HttpType.POST    , "path": "/user/ban"                              },
    "getBannedPersons":                     { "method": HttpType.GET     , "path": "/user/banned"                           },
    "blockPerson":                          { "method": HttpType.POST    , "path": "/user/block"                            },
    "deleteAccount":                        { "method": HttpType.POST    , "path": "/user/delete_account"                   },
    "passwordReset":                        { "method": HttpType.POST    , "path": "/user/password_reset"                   },
    "passwordChangeAfterReset":             { "method": HttpType.POST    , "path": "/user/password_change"                  },
    "saveUserSettings":                     { "method": HttpType.PUT     , "path": "/user/save_user_settings"               },
    "markAllAsRead":                        { "method": HttpType.GET     , "path": "/user/mark_all_as_read"                 },
    "changePassword":                       { "method": HttpType.PUT     , "path": "/user/change_password"                  },
    "getReportCount":                       { "method": HttpType.GET     , "path": "/user/report_count"                     },
    "getUnreadCount":                       { "method": HttpType.GET     , "path": "/user/unread_count"                     },
    "verifyEmail":                          { "method": HttpType.POST    , "path": "/user/verify_email"                     },
    "addAdmin":                             { "method": HttpType.POST    , "path": "/admin/add"                             },
    "getUnreadRegistrationApplicationCount":{ "method": HttpType.GET     , "path": "/admin/registration_application/count"  },
    "listRegistrationApplications":         { "method": HttpType.GET     , "path": "/admin/registration_application/list"   },
    "createCustomEmoji":                    { "method": HttpType.GET     , "path": "/custom_emoji"                          },
    "editCustomEmoji":                      { "method": HttpType.PUT     , "path": "/custom_emoji"                          },
    "deleteCustomEmoji":                    { "method": HttpType.POST    , "path": "/custom_emoji/delete"                   },
    "addModToCommunity":                    { "method": HttpType.POST    , "path": "/community/mod"                         },
    "approveRegistrationApplication":       { "method": HttpType.PUT     , "path": "/admin/registration_application/approve"},
    "blockCommunity":                       { "method": HttpType.POST    , "path": "/community/block"                       },
    "createCommentReport":                  { "method": HttpType.POST    , "path": "/comment/report"                        },
    "createCommunity":                      { "method": HttpType.POST    , "path": "/community"                             },
    "createPostReport":                     { "method": HttpType.POST    , "path": "/post/report"                           },
    "createPrivateMessage":                 { "method": HttpType.POST    , "path": "/private_message"                       },
    "createPrivateMessageReport":           { "method": HttpType.POST    , "path": "/private_message/report"                },
    "editPrivateMessage":                   { "method": HttpType.PUT     , "path": "/private_message"                       },
    "deletePrivateMessage":                 { "method": HttpType.POST    , "path": "/private_message/delete"                },
    "markPrivateMessageAsRead":             { "method": HttpType.POST    , "path": "/private_message/mark_as_read"          },
    "deleteComment":                        { "method": HttpType.POST    , "path": "/comment/delete"                        },
    "deleteCommunity":                      { "method": HttpType.POST    , "path": "/community/delete"                      },
    "removeComment":                        { "method": HttpType.POST    , "path": "/comment/remove"                        },
    "deletePost":                           { "method": HttpType.POST    , "path": "/post/delete"                           },
    "distinguishComment":                   { "method": HttpType.POST    , "path": "/comment/distinguish"                   },
    "editComment":                          { "method": HttpType.PUT     , "path": "/comment"                               },
    "editCommunity":                        { "method": HttpType.PUT     , "path": "/community"                             },
    "banFromCommunity":                     { "method": HttpType.POST    , "path": "/community/ban_user"                    },
    "editSite":                             { "method": HttpType.PUT     , "path": "/site"                                  },
    "featurePost":                          { "method": HttpType.POST    , "path": "/post/feature"                          },
    "getFederatedInstances":                { "method": HttpType.GET     , "path": "/federated_instances"                   },
    "createSite":                           { "method": HttpType.POST    , "path": "/site"                                  },
    "getCaptcha":                           { "method": HttpType.GET     , "path": "/user/get_captcha"                      },
    "getComment":                           { "method": HttpType.GET     , "path": "/comment"                               },
    "getComments":                          { "method": HttpType.GET     , "path": "/comment/list"                          },
    "getModlog":                            { "method": HttpType.GET     , "path": "/modlog"                                },
    "getPrivateMessages":                   { "method": HttpType.GET     , "path": "/private_message/list"                  },
    "listCommentReports":                   { "method": HttpType.GET     , "path": "/comment/report/list"                   },
    "listPostReports":                      { "method": HttpType.GET     , "path": "/post/report/list"                      },
    "listPrivateMessageReports":            { "method": HttpType.GET     , "path": "/private_message/report/list"           },
    "lockPost":                             { "method": HttpType.POST    , "path": "/post/lock"                             },
    "markCommentReplyAsRead":               { "method": HttpType.POST    , "path": "/comment/mark_as_read"                  },
    "markPostAsRead":                       { "method": HttpType.POST    , "path": "/post/mark_as_read"                     },
    "purgeComment":                         { "method": HttpType.POST    , "path": "/admin/purge/comment"                   },
    "purgeCommunity":                       { "method": HttpType.POST    , "path": "/admin/purge/community"                 },
    "purgePost":                            { "method": HttpType.POST    , "path": "/admin/purge/post"                      },
    "purgePerson":                          { "method": HttpType.POST    , "path": "/admin/purge/person"                    },
    "removeCommunity":                      { "method": HttpType.POST    , "path": "/community/remove"                      },
    "resolveCommentReport":                 { "method": HttpType.PUT     , "path": "/comment/report/resolve"                },
    "resolvePostReport":                    { "method": HttpType.PUT     , "path": "/post/report/resolve"                   },
    "resolvePrivateMessageReport":          { "method": HttpType.PUT     , "path": "/private_message/report/resolve"        },
    "saveComment":                          { "method": HttpType.PUT     , "path": "/comment/save"                          },
    "savePost":                             { "method": HttpType.PUT     , "path": "/post/save"                             },
    "transferCommunity":                    { "method": HttpType.POST    , "path": "/community/transfer"                    },
    "getSiteMetadata":                      { "method": HttpType.GET     , "path": "/post/site_metadata"                    },
    "removePost":                           { "method": HttpType.POST    , "path": "/post/remove"                           },
}

